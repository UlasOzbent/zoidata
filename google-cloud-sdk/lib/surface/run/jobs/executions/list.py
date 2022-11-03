# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command for listing job executions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.command_lib.run import commands
from googlecloudsdk.command_lib.run import connection_context
from googlecloudsdk.command_lib.run import flags
from googlecloudsdk.command_lib.run import pretty_print
from googlecloudsdk.command_lib.run import resource_args
from googlecloudsdk.command_lib.run import serverless_operations
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.command_lib.util.concepts import presentation_specs


def _SucceededStatus(execution):
  return '{} / {}'.format(
      execution.get('status', {}).get('succeededCount', 0),
      execution.get('spec', {}).get('taskCount', 0))


def _ByStartAndCreationTime(ex):
  """Sort key that sorts executions by start time, newest and unstarted first.

  All unstarted executions will be first and sorted by their creation timestamp,
  all started executions will be second and sorted by their start time.

  Args:
    ex: googlecloudsdk.api_lib.run.execution.Execution

  Returns:
    The lastTransitionTime of the Started condition or the creation timestamp of
    the execution if the execution is unstarted.
  """
  return (False if ex.started_condition and
          ex.started_condition['status'] is not None else True,
          ex.started_condition['lastTransitionTime']
          if ex.started_condition else ex.creation_timestamp)


class List(commands.List):
  """List executions."""

  detailed_help = {
      'DESCRIPTION':
          """
          {description}
          """,
      'EXAMPLES':
          """
          To list all executions in all regions:

              $ {command}
         """,
  }

  @classmethod
  def CommonArgs(cls, parser):
    namespace_presentation = presentation_specs.ResourcePresentationSpec(
        '--namespace',
        resource_args.GetNamespaceResourceSpec(),
        'Namespace to list executions in.',
        required=True,
        prefixes=False)
    flags.AddJobFlag(parser)
    concept_parsers.ConceptParser([namespace_presentation]).AddToParser(parser)
    parser.display_info.AddFormat(
        'table('
        '{ready_column},'
        'job_name:label=JOB,'
        'name:label=EXECUTION,'
        'region:label=REGION,'
        'status.runningCount.yesno(no="0"):label=RUNNING,'
        'succeeded_status():label=COMPLETE,'
        'creation_timestamp.date("%Y-%m-%d %H:%M:%S %Z"):label=CREATED,'
        'author:label="RUN BY")'.format(ready_column=pretty_print.READY_COLUMN))
    parser.display_info.AddUriFunc(cls._GetResourceUri)
    parser.display_info.AddTransforms({
        'succeeded_status': _SucceededStatus,
    })

  @classmethod
  def Args(cls, parser):
    cls.CommonArgs(parser)

  def _SortExecutions(self, executions):
    return sorted(
        commands.SortByName(executions),
        key=_ByStartAndCreationTime,
        reverse=True)

  def Run(self, args):
    """List executions of a job."""
    job_name = args.job
    namespace_ref = args.CONCEPTS.namespace.Parse()
    conn_context = connection_context.GetConnectionContext(
        args, flags.Product.RUN, self.ReleaseTrack())
    with serverless_operations.Connect(conn_context) as client:
      self.SetCompleteApiEndpoint(conn_context.endpoint)
      return self._SortExecutions(
          client.ListExecutions(namespace_ref, job_name))

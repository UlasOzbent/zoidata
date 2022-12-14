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
"""Generic command to enable any Hub Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base as sdk_base
from googlecloudsdk.command_lib.container.fleet.features import base


@sdk_base.Hidden
class Enable(base.EnableCommand):
  """Enable a Hub Feature.

  ## EXAMPLES

  To enable the `metering` feature, run:

    $ {command} metering
  """

  @staticmethod
  def Args(parser):
    parser.add_argument(
        'feature',
        help='Short name of the Feature to enable.',
    )

  def Run(self, args):
    self.feature_name = args.feature
    self.Enable(self.messages.Feature())

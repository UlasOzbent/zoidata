"""Generated client library for dns version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from samples.dns_sample.dns_v1 import dns_v1_messages as messages


class DnsV1(base_api.BaseApiClient):
  """Generated client library for service dns version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://www.googleapis.com/dns/v1/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'dns'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only', u'https://www.googleapis.com/auth/ndev.clouddns.readonly', u'https://www.googleapis.com/auth/ndev.clouddns.readwrite']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'DnsV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new dns handle."""
    url = url or self.BASE_URL
    super(DnsV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.changes = self.ChangesService(self)
    self.managedZones = self.ManagedZonesService(self)
    self.projects = self.ProjectsService(self)
    self.resourceRecordSets = self.ResourceRecordSetsService(self)

  class ChangesService(base_api.BaseApiService):
    """Service class for the changes resource."""

    _NAME = u'changes'

    def __init__(self, client):
      super(DnsV1.ChangesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Atomically update the ResourceRecordSet collection.

      Args:
        request: (DnsChangesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Change) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dns.changes.create',
        ordered_params=[u'project', u'managedZone'],
        path_params=[u'managedZone', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/managedZones/{managedZone}/changes',
        request_field=u'change',
        request_type_name=u'DnsChangesCreateRequest',
        response_type_name=u'Change',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Fetch the representation of an existing Change.

      Args:
        request: (DnsChangesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Change) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dns.changes.get',
        ordered_params=[u'project', u'managedZone', u'changeId'],
        path_params=[u'changeId', u'managedZone', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/managedZones/{managedZone}/changes/{changeId}',
        request_field='',
        request_type_name=u'DnsChangesGetRequest',
        response_type_name=u'Change',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Enumerate Changes to a ResourceRecordSet collection.

      Args:
        request: (DnsChangesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ChangesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dns.changes.list',
        ordered_params=[u'project', u'managedZone'],
        path_params=[u'managedZone', u'project'],
        query_params=[u'maxResults', u'pageToken', u'sortBy', u'sortOrder'],
        relative_path=u'projects/{project}/managedZones/{managedZone}/changes',
        request_field='',
        request_type_name=u'DnsChangesListRequest',
        response_type_name=u'ChangesListResponse',
        supports_download=False,
    )

  class ManagedZonesService(base_api.BaseApiService):
    """Service class for the managedZones resource."""

    _NAME = u'managedZones'

    def __init__(self, client):
      super(DnsV1.ManagedZonesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new ManagedZone.

      Args:
        request: (DnsManagedZonesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZone) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dns.managedZones.create',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[],
        relative_path=u'projects/{project}/managedZones',
        request_field=u'managedZone',
        request_type_name=u'DnsManagedZonesCreateRequest',
        response_type_name=u'ManagedZone',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete a previously created ManagedZone.

      Args:
        request: (DnsManagedZonesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DnsManagedZonesDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'dns.managedZones.delete',
        ordered_params=[u'project', u'managedZone'],
        path_params=[u'managedZone', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/managedZones/{managedZone}',
        request_field='',
        request_type_name=u'DnsManagedZonesDeleteRequest',
        response_type_name=u'DnsManagedZonesDeleteResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Fetch the representation of an existing ManagedZone.

      Args:
        request: (DnsManagedZonesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZone) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dns.managedZones.get',
        ordered_params=[u'project', u'managedZone'],
        path_params=[u'managedZone', u'project'],
        query_params=[],
        relative_path=u'projects/{project}/managedZones/{managedZone}',
        request_field='',
        request_type_name=u'DnsManagedZonesGetRequest',
        response_type_name=u'ManagedZone',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Enumerate ManagedZones that have been created but not yet deleted.

      Args:
        request: (DnsManagedZonesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ManagedZonesListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dns.managedZones.list',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[u'dnsName', u'maxResults', u'pageToken'],
        relative_path=u'projects/{project}/managedZones',
        request_field='',
        request_type_name=u'DnsManagedZonesListRequest',
        response_type_name=u'ManagedZonesListResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(DnsV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Fetch the representation of an existing Project.

      Args:
        request: (DnsProjectsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Project) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dns.projects.get',
        ordered_params=[u'project'],
        path_params=[u'project'],
        query_params=[],
        relative_path=u'projects/{project}',
        request_field='',
        request_type_name=u'DnsProjectsGetRequest',
        response_type_name=u'Project',
        supports_download=False,
    )

  class ResourceRecordSetsService(base_api.BaseApiService):
    """Service class for the resourceRecordSets resource."""

    _NAME = u'resourceRecordSets'

    def __init__(self, client):
      super(DnsV1.ResourceRecordSetsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Enumerate ResourceRecordSets that have been created but not yet deleted.

      Args:
        request: (DnsResourceRecordSetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResourceRecordSetsListResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dns.resourceRecordSets.list',
        ordered_params=[u'project', u'managedZone'],
        path_params=[u'managedZone', u'project'],
        query_params=[u'maxResults', u'name', u'pageToken', u'type'],
        relative_path=u'projects/{project}/managedZones/{managedZone}/rrsets',
        request_field='',
        request_type_name=u'DnsResourceRecordSetsListRequest',
        response_type_name=u'ResourceRecordSetsListResponse',
        supports_download=False,
    )

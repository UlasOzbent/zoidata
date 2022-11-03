"""Generated client library for policysimulator version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.policysimulator.v1alpha import policysimulator_v1alpha_messages as messages


class PolicysimulatorV1alpha(base_api.BaseApiClient):
  """Generated client library for service policysimulator version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://policysimulator.googleapis.com/'
  MTLS_BASE_URL = 'https://policysimulator.mtls.googleapis.com/'

  _PACKAGE = 'policysimulator'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'PolicysimulatorV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new policysimulator handle."""
    url = url or self.BASE_URL
    super(PolicysimulatorV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations = self.OperationsService(self)
    self.organizations_locations_orgPolicyViolationsPreviews_orgPolicyViolations = self.OrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsService(self)
    self.organizations_locations_orgPolicyViolationsPreviews = self.OrganizationsLocationsOrgPolicyViolationsPreviewsService(self)
    self.organizations_locations = self.OrganizationsLocationsService(self)
    self.organizations = self.OrganizationsService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(PolicysimulatorV1alpha.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (PolicysimulatorOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/operations/{operationsId}',
        http_method='GET',
        method_id='policysimulator.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='PolicysimulatorOperationsGetRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (PolicysimulatorOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='policysimulator.operations.list',
        ordered_params=[],
        path_params=[],
        query_params=['filter', 'name', 'pageSize', 'pageToken'],
        relative_path='v1alpha/operations',
        request_field='',
        request_type_name='PolicysimulatorOperationsListRequest',
        response_type_name='GoogleLongrunningListOperationsResponse',
        supports_download=False,
    )

  class OrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsService(base_api.BaseApiService):
    """Service class for the organizations_locations_orgPolicyViolationsPreviews_orgPolicyViolations resource."""

    _NAME = 'organizations_locations_orgPolicyViolationsPreviews_orgPolicyViolations'

    def __init__(self, client):
      super(PolicysimulatorV1alpha.OrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""ListOrgPolicyViolations lists the OrgPolicyViolations that are present in an OrgPolicyViolationsPreview.

      Args:
        request: (PolicysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/organizations/{organizationsId}/locations/{locationsId}/orgPolicyViolationsPreviews/{orgPolicyViolationsPreviewsId}/orgPolicyViolations',
        http_method='GET',
        method_id='policysimulator.organizations.locations.orgPolicyViolationsPreviews.orgPolicyViolations.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/orgPolicyViolations',
        request_field='',
        request_type_name='PolicysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsOrgPolicyViolationsListRequest',
        response_type_name='GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsResponse',
        supports_download=False,
    )

  class OrganizationsLocationsOrgPolicyViolationsPreviewsService(base_api.BaseApiService):
    """Service class for the organizations_locations_orgPolicyViolationsPreviews resource."""

    _NAME = 'organizations_locations_orgPolicyViolationsPreviews'

    def __init__(self, client):
      super(PolicysimulatorV1alpha.OrganizationsLocationsOrgPolicyViolationsPreviewsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""GetOrgPolicyViolationsPreview gets the specified OrgPolicyViolationsPreview. Each OrgPolicyViolationsPreview is available for at least 7 days.

      Args:
        request: (PolicysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/organizations/{organizationsId}/locations/{locationsId}/orgPolicyViolationsPreviews/{orgPolicyViolationsPreviewsId}',
        http_method='GET',
        method_id='policysimulator.organizations.locations.orgPolicyViolationsPreviews.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='PolicysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsGetRequest',
        response_type_name='GoogleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""ListOrgPolicyViolationsPreviews lists each OrgPolicyViolationsPreview in an organization. Each OrgPolicyViolationsPreview is available for at least 7 days.

      Args:
        request: (PolicysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/organizations/{organizationsId}/locations/{locationsId}/orgPolicyViolationsPreviews',
        http_method='GET',
        method_id='policysimulator.organizations.locations.orgPolicyViolationsPreviews.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/orgPolicyViolationsPreviews',
        request_field='',
        request_type_name='PolicysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsListRequest',
        response_type_name='GoogleCloudPolicysimulatorV1alphaListOrgPolicyViolationsPreviewsResponse',
        supports_download=False,
    )

  class OrganizationsLocationsService(base_api.BaseApiService):
    """Service class for the organizations_locations resource."""

    _NAME = 'organizations_locations'

    def __init__(self, client):
      super(PolicysimulatorV1alpha.OrganizationsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def OrgPolicyViolationsPreviews(self, request, global_params=None):
      r"""GenerateOrgPolicyViolationsPreview generates an OrgPolicyViolationsPreview for the proposed changes in the provided OrgPolicyViolationsPreview.OrgPolicyOverlay. The changes to OrgPolicy are specified by this `OrgPolicyOverlay`. The resources to scan are inferred from these specified changes.

      Args:
        request: (PolicysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('OrgPolicyViolationsPreviews')
      return self._RunMethod(
          config, request, global_params=global_params)

    OrgPolicyViolationsPreviews.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/organizations/{organizationsId}/locations/{locationsId}/orgPolicyViolationsPreviews',
        http_method='POST',
        method_id='policysimulator.organizations.locations.orgPolicyViolationsPreviews',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha/{+parent}/orgPolicyViolationsPreviews',
        request_field='googleCloudPolicysimulatorV1alphaOrgPolicyViolationsPreview',
        request_type_name='PolicysimulatorOrganizationsLocationsOrgPolicyViolationsPreviewsRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = 'organizations'

    def __init__(self, client):
      super(PolicysimulatorV1alpha.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

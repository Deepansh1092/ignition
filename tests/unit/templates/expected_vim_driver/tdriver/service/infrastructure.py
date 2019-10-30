import ignition.model.infrastructure as infrastructure_model
from ignition.service.framework import Service
from ignition.service.infrastructure import InfrastructureDriverCapability

class InfrastructureDriver(Service, InfrastructureDriverCapability):

    def create_infrastructure(self, template, template_type, inputs, deployment_location):
        """
        Initiates a request to create infrastructure based on a TOSCA template.
        This method should return immediate response of the request being accepted,
        it is expected that the InfrastructureService will poll get_infrastructure_task on this driver to determine when the request has complete.

        :param str template: template of infrastructure to be created
        :param str template_type: type of template used i.e. TOSCA or Heat
        :param str inputs: values for the inputs defined on the tosca template
        :param dict deployment_location: the deployment location to deploy to
        :return: an ignition.model.infrastructure.CreateInfrastructureResponse
        """
        print("Creating some Infrastructure")
        infrastructure_id = '1'
        request_id = '1'
        return infrastructure_model.CreateInfrastructureResponse(infrastructure_id, request_id)

    def get_infrastructure_task(self, infrastructure_id, request_id, deployment_location):
        """
        Get information about the infrastructure (created or deleted)

        :param str infrastructure_id: identifier of the infrastructure to check
        :param str request_id: identifier of the request to check
        :param dict deployment_location: the location the infrastructure was deployed to
        :return: an ignition.model.infrastructure.InfrastructureTask instance describing the status
        """
        print("Querying some Infrastructure")
        return infrastructure_model.InfrastructureTask(infrastructure_id, request_id, infrastructure_model.STATUS_IN_PROGRESS)

    def delete_infrastructure(self, infrastructure_id, deployment_location):
        """
        Initiates a request to delete infrastructure previously created with the given infrastructure_id.
        This method should return immediate response of the request being accepted,
        it is expected that the InfrastructureService will poll get_infrastructure_task on this driver to determine when the request has complete.

        :param str infrastructure_id: identifier of the infrastructure to be removed
        :param dict deployment_location: the location the infrastructure was deployed to
        :return: an ignition.model.infrastructure.DeleteInfrastructureResponse
        """
        print("Deleting some Infrastructure")
        request_id = '2'
        return infrastructure_model.DeleteInfrastructureResponse(infrastructure_id, request_id)

    def find_infrastructure(self, template, template_type, instance_name, deployment_location):
        """
        Finds infrastructure instances that meet the requirements set out in the given TOSCA template, returning the desired output values from those instances

        :param str template: tosca template of infrastructure to be found
        :param str template_type: type of template used i.e. TOSCA or Heat
        :param str instance_name: name given as search criteria
        :param dict deployment_location: the deployment location to deploy to
        :return: an ignition.model.infrastructure.FindInfrastructureResponse
        """
        print("Finding some Infrastructure")
        return infrastructure_model.FindInfrastructureResponse()
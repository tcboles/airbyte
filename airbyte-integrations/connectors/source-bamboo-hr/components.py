#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

from dataclasses import InitVar, dataclass
from typing import Any, Mapping

from airbyte_cdk.sources.declarative.interpolation.interpolated_string import InterpolatedString
from airbyte_cdk.sources.declarative.schema.json_file_schema_loader import JsonFileSchemaLoader, _default_file_path


@dataclass
class CustomReportsSchemaLoader(JsonFileSchemaLoader):
    config: Mapping[str, Any]
    parameters: InitVar[Mapping[str, Any]] = {"name": "custom_reports_stream"}

    def __post_init__(self, parameters: Mapping[str, Any]):
        if not self.file_path:
            self.file_path = _default_file_path()
        self.file_path = InterpolatedString.create(self.file_path, parameters=self.parameters)

    def get_json_schema(self) -> Mapping[str, Any]:
        """
        Returns the JSON schema.

        The final schema is constructed by first generating a schema for the fields
        in the config and, if default fields should be included, adding these to the
        schema.
        """
        schema = self._get_json_schema_from_config()
        if self.config.get("custom_reports_include_default_fields"):
            default_schema = CUSTOM_REPORTS_BASE_SCHEMA
            schema = self._union_schemas(default_schema, schema)
        return schema

    def _get_json_schema_from_config(self):
        if self.config.get("custom_reports_fields"):
            properties = {
                field.strip(): {"type": ["null", "string"]}
                for field in self.convert_custom_reports_fields_to_list(self.config.get("custom_reports_fields", ""))
            }
        else:
            properties = {}
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": properties,
        }

    def convert_custom_reports_fields_to_list(self, custom_reports_fields: str) -> list:
        return custom_reports_fields.split(",") if custom_reports_fields else []

    def _union_schemas(self, schema1, schema2):
        schema1["properties"] = {**schema1["properties"], **schema2["properties"]}
        return schema1


CUSTOM_REPORTS_BASE_SCHEMA = {
    "type": ["null", "object"],
    "required": [],
    "properties": {
        "acaStatus": {"description": "The Affordable Care Act status of the employee.", "type": ["null", "string"]},
        "acaStatusCategory": {"description": "The category of the Affordable Care Act status of the employee.", "type": ["null", "string"]},
        "address1": {"description": "First line of the employee's address.", "type": ["null", "string"]},
        "address2": {"description": "Second line of the employee's address.", "type": ["null", "string"]},
        "age": {"description": "The age of the employee.", "type": ["null", "string"]},
        "bestEmail": {"description": "The primary email address of the employee.", "type": ["null", "string"]},
        "birthday": {"description": "The birthday of the employee.", "type": ["null", "string"]},
        "bonusAmount": {"description": "The amount of bonus received by the employee.", "type": ["null", "string"]},
        "bonusComment": {"description": "Comment related to the bonus received by the employee.", "type": ["null", "string"]},
        "bonusDate": {"description": "Date on which the bonus was received by the employee.", "type": ["null", "string"]},
        "bonusReason": {"description": "Reason for granting the bonus to the employee.", "type": ["null", "string"]},
        "city": {"description": "City where the employee is located.", "type": ["null", "string"]},
        "commissionAmount": {"description": "The amount of commission received by the employee.", "type": ["null", "string"]},
        "commissionComment": {"description": "Comment related to the commission received by the employee.", "type": ["null", "string"]},
        "commissionDate": {"description": "Date on which the commission was received by the employee.", "type": ["null", "string"]},
        "commisionDate": {"description": "Date of commission for the employee.", "type": ["null", "string"]},
        "country": {"description": "Country where the employee is located.", "type": ["null", "string"]},
        "createdByUserId": {"description": "ID of the user who created the employee record.", "type": ["null", "string"]},
        "dateOfBirth": {"description": "Date of birth of the employee.", "type": ["null", "string"]},
        "department": {"description": "Department in which the employee works.", "type": ["null", "string"]},
        "division": {"description": "Division to which the employee belongs.", "type": ["null", "string"]},
        "eeo": {"description": "Equal Employment Opportunity (EEO) information of the employee.", "type": ["null", "string"]},
        "employeeNumber": {"description": "Unique employee identification number.", "type": ["null", "string"]},
        "employmentHistoryStatus": {"description": "Status of the employee's employment history.", "type": ["null", "string"]},
        "ethnicity": {"description": "Ethnicity information of the employee.", "type": ["null", "string"]},
        "exempt": {"description": "Exempt status of the employee for employment regulations.", "type": ["null", "string"]},
        "firstName": {"description": "First name of the employee.", "type": ["null", "string"]},
        "flsaCode": {"description": "Fair Labor Standards Act (FLSA) code classification of the employee.", "type": ["null", "string"]},
        "fullName1": {"description": "First version of the employee's full name.", "type": ["null", "string"]},
        "fullName2": {"description": "Second version of the employee's full name.", "type": ["null", "string"]},
        "fullName3": {"description": "Third version of the employee's full name.", "type": ["null", "string"]},
        "fullName4": {"description": "Fourth version of the employee's full name.", "type": ["null", "string"]},
        "fullName5": {"description": "Fifth version of the employee's full name.", "type": ["null", "string"]},
        "displayName": {"description": "Display name of the employee.", "type": ["null", "string"]},
        "gender": {"description": "Gender of the employee.", "type": ["null", "string"]},
        "hireDate": {"description": "Date on which the employee was hired.", "type": ["null", "string"]},
        "originalHireDate": {"description": "Original hire date of the employee.", "type": ["null", "string"]},
        "homeEmail": {"description": "Home email address of the employee.", "type": ["null", "string"]},
        "homePhone": {"description": "Home phone number of the employee.", "type": ["null", "string"]},
        "id": {"description": "Unique identifier of the employee.", "type": ["null", "string"]},
        "isPhotoUploaded": {"description": "Indicator if the employee's photo is uploaded in the system.", "type": ["null", "string"]},
        "jobTitle": {"description": "Title of the employee's job position.", "type": ["null", "string"]},
        "lastChanged": {"description": "Date of the last change made to the employee's record.", "type": ["null", "string"]},
        "lastName": {"description": "Last name of the employee.", "type": ["null", "string"]},
        "location": {"description": "Physical location where the employee works.", "type": ["null", "string"]},
        "maritalStatus": {"description": "Marital status of the employee.", "type": ["null", "string"]},
        "middleName": {"description": "Middle name of the employee.", "type": ["null", "string"]},
        "mobilePhone": {"description": "Mobile phone number of the employee.", "type": ["null", "string"]},
        "nationalId": {"description": "National identification number of the employee.", "type": ["null", "string"]},
        "nationality": {"description": "Nationality information of the employee.", "type": ["null", "string"]},
        "nin": {"description": "National Insurance Number (NIN) of the employee.", "type": ["null", "string"]},
        "payChangeReason": {"description": "Reason for a change in payment for the employee.", "type": ["null", "string"]},
        "payGroup": {"description": "Group to which the employee's payment belongs.", "type": ["null", "string"]},
        "payGroupId": {"description": "ID of the payment group for the employee.", "type": ["null", "string"]},
        "payRate": {"description": "Rate of pay for the employee.", "type": ["null", "string"]},
        "payRateEffectiveDate": {"description": "Date from which the pay rate is effective for the employee.", "type": ["null", "string"]},
        "payType": {"description": "Type of payment for the employee.", "type": ["null", "string"]},
        "paidPer": {"description": "Frequency at which the employee is paid.", "type": ["null", "string"]},
        "paySchedule": {"description": "Schedule according to which the employee is paid.", "type": ["null", "string"]},
        "payScheduleId": {"description": "ID of the payment schedule for the employee.", "type": ["null", "string"]},
        "payFrequency": {"description": "Frequency of payment for the employee.", "type": ["null", "string"]},
        "includeInPayroll": {"description": "Indicator if the employee is included in the payroll system.", "type": ["null", "string"]},
        "timeTrackingEnabled": {"description": "Indicator if time tracking is enabled for the employee.", "type": ["null", "string"]},
        "preferredName": {"description": "Preferred name of the employee.", "type": ["null", "string"]},
        "ssn": {"description": "Social Security Number (SSN) of the employee.", "type": ["null", "string"]},
        "sin": {"description": "Social Insurance Number (SIN) of the employee.", "type": ["null", "string"]},
        "standardHoursPerWeek": {"description": "Standard number of hours worked by the employee per week.", "type": ["null", "string"]},
        "state": {"description": "State where the employee is located.", "type": ["null", "string"]},
        "stateCode": {"description": "Code representing the state where the employee is located.", "type": ["null", "string"]},
        "status": {"description": "Employment status of the employee.", "type": ["null", "string"]},
        "supervisor": {"description": "Name of the employee's supervisor.", "type": ["null", "string"]},
        "supervisorId": {"description": "ID of the employee's supervisor.", "type": ["null", "string"]},
        "supervisorEId": {"description": "Employee ID of the employee's supervisor.", "type": ["null", "string"]},
        "supervisorEmail": {"description": "Email address of the employee's supervisor.", "type": ["null", "string"]},
        "terminationDate": {"description": "Date on which the employee was terminated.", "type": ["null", "string"]},
        "workEmail": {"description": "Work email address of the employee.", "type": ["null", "string"]},
        "workPhone": {"description": "Work phone number of the employee.", "type": ["null", "string"]},
        "workPhonePlusExtension": {
            "description": "Full work phone number including extension for the employee.",
            "type": ["null", "string"],
        },
        "workPhoneExtension": {"description": "Extension number for the employee's work phone.", "type": ["null", "string"]},
        "zipcode": {"description": "Zip code of the employee's location.", "type": ["null", "string"]},
    },
}

from typing import List, Optional

class Stage:
    def __init__(self, name: str, label: str, description: str, order: int):
        self.name = name
        self.label = label
        self.description = description
        self.order = order


class CustomerPortalCreateRequest:
    def __init__(self, customerEmail: str, customerName: str, customerPhone: str, projectName: str, stages: List[Stage],
                 address1: Optional[str] = None, city: Optional[str] = None, stateCode: Optional[str] = None,
                 zip: Optional[str] = None, address2: Optional[str] = None, projectContactEmail: Optional[str] = None,
                 projectContactPhone: Optional[str] = None, enableReferrals: Optional[bool] = False):
        self.customerEmail = customerEmail
        self.customerName = customerName
        self.customerPhone = customerPhone
        self.projectName = projectName
        self.stages = stages
        self.address1 = address1
        self.city = city
        self.stateCode = stateCode
        self.zip = zip
        self.address2 = address2
        self.projectContactEmail = projectContactEmail
        self.projectContactPhone = projectContactPhone
        self.enableReferrals = enableReferrals


    def to_dict(self) -> dict:
        """
        Convert the model object to a dictionary.
        """
        return {key: value for key, value in self.__dict__.items() if value is not None}

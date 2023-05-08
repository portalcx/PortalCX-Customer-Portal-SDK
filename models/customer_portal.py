from typing import Dict

class CustomerPortal:
    def __init__(self, portal_id: str, name: str, url: str, description: str):
        self.portal_id = portal_id
        self.name = name
        self.url = url
        self.description = description

    @classmethod
    def from_dict(cls, data: Dict) -> "CustomerPortal":
        portal_id = data.get("portal_id")
        name = data.get("name")
        url = data.get("url")
        description = data.get("description")
        return cls(portal_id, name, url, description)

    def to_dict(self) -> Dict:
        return {
            "portal_id": self.portal_id,
            "name": self.name,
            "url": self.url,
            "description": self.description,
        }
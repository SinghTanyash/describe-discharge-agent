from pydantic import BaseModel


class Medication(BaseModel):

    name: str

    frequency: str = ""

    duration: str = ""

    quantity: str = ""
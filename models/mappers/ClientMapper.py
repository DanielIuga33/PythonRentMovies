from models.Client import Client
from models.dto.ClientDto import ClientDto


class ClientMapper:
    def fromEntityToDto(self, entity: Client):
        return ClientDto(entity.get_name(), entity.get_surname(), entity.get_email())

    def fromListsEntityToDtoList(self, entity_list):
        result = []
        for entity in entity_list:
            result.append(ClientDto(entity.get_id_entity(), entity.get_name(), entity.get_surname(),
                                    entity.get_email()))
        return result

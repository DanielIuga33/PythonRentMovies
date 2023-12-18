from models.Client import Client
from models.dto.ClientDto import ClientDto


class ClientMapper:
    def fromEntityToDto(self, entity: Client):
        return ClientDto(entity.get_client_id(), entity.get_name(), entity.get_surname(), entity.get_email())

    def fromListsEntityToDtoList(self, entityLists):
        result = []
        for entity in entityLists:
            result.append(ClientDto(entity.get_client_id(), entity.get_name(), entity.get_surname(),
                                    entity.get_email()))
        return result

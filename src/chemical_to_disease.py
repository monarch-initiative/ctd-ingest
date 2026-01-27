import uuid
import koza
from biolink_model.datamodel.pydanticmodel_v2 import (
    ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation,
    KnowledgeLevelEnum,
    AgentTypeEnum,
)


@koza.transform_record()
def transform_record(koza_transform, row):
    if row['DirectEvidence'] in ['therapeutic']:

        chemical_id = 'MESH:' + row['ChemicalID']
        disease_id = row['DiseaseID']

        predicate = "biolink:treats_or_applied_or_studied_to_treat"

        association = ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation(
            id="uuid:" + str(uuid.uuid1()),
            subject=chemical_id,
            predicate=predicate,
            object=disease_id,
            publications=["PMID:" + p for p in row['PubMedIDs'].split("|")] if row['PubMedIDs'] else None,
            aggregator_knowledge_source=["infores:monarchinitiative"],
            primary_knowledge_source="infores:ctd",
            knowledge_level=KnowledgeLevelEnum.knowledge_assertion,
            agent_type=AgentTypeEnum.manual_agent,
        )

        return [association]

    return []

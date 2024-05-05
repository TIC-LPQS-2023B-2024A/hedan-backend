from src.modules.questionnaires.domain.entities.child import Child
from src.modules.questionnaires.domain.entities.psychologist import Psychologist
from src.modules.questionnaires.domain.entities.questionnaire_response import QuestionnaireResponse
from src.modules.questionnaires.domain.value_objects.answer import Answer
from src.modules.questionnaires.domain.value_objects.scholar_grade import ScholarGrade


class QuestionnairesService:
    @staticmethod
    def register_child_by_psychologist(child: Child, psychologist: Psychologist):
        psychologist.add_child(child)

    @staticmethod
    def register_child_questionnaire_response_by_psychologist(
            child: Child,
            psychologist: Psychologist,
            child_age: int,
            child_scholar_grade: int,
            reason: str,
            referrer: str,
            answers: tuple[Answer, ...]
    ):
        questionnaire_response = QuestionnaireResponse(
            child_age=child_age,
            child_scholar_grade=ScholarGrade(child_scholar_grade),
            reason=reason,
            referrer=referrer,
            answers=answers,
            psychologist_id=psychologist.cedula,
            child_id=child.cedula
        )
        child.add_questionnaire_response(questionnaire_response)
        psychologist.add_questionnaire_response(questionnaire_response)

"""
-- Created by Bikash Saud
-- Treeleaf Technologies Pvt. Ltd.
-- Created on 2022-12-10
"""
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Category, Quizzes, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")



class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = "__all__"


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = "__all__"



class Query(graphene.ObjectType):\
    # NOte: DjangoListField to return List of data without write resolver.
    # all_quizzes = DjangoListField(QuizzesType)

    # def resolve_all_quizzes(root, info): # this can customize your query but all quizzes also return all list data
    #     return Quizzes.objects.all()
    # filter by id
    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    def resolve_all_quizzes(root, info, id):
        return Quizzes.objects.get  (pk=id)

    # Bring Answers
    # List = Retiurn list of data
    answer_list = graphene.List(AnswerType, id=graphene.Int())
    def resolve_answer_list(root, info, id):
        return Answer.objects.filter(question=id)


    # for all questions:
    # for list of question
    # question_list = DjangoListField(QuestionType)

    # def resolve_question_list(root, info):
    #     return Question.objects.all()
    # get question by id
    # NOTE: Field return only on data.
    question_list = graphene.Field(QuestionType, id=graphene.Int())

    def resolve_question_list(root, info, id):
        return Question.objects.get(id=id)

    
    # old way
    # all_quizzes = graphene.List(QuizzesType)
    # def resolve_all_quizzes(root,info):
    #     return Quizzes.objects.all()

class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    category = graphene.Field(CategoryType)
    @classmethod
    def mutate(cls, root,info, name):
        print(name, 999)
        category = Category(name = name)
        category.save()
        return CategoryMutation(category=category)
class CategoryAddMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()
    category = graphene.Field(CategoryType)
    @classmethod
    def mutate(cls, root,info, name, id):
        print(name, 999)
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryMutation(category=category)


class CategoryDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        print(id, 999)
        category = Category.objects.get(id=id)
        category.delete()
        return CategoryMutation(category=category)

class Mutation(graphene.ObjectType):
    add_category = CategoryMutation.Field()
    update_category= CategoryAddMutation.Field()
    delete_category = CategoryDeleteMutation.Field()


schema = graphene.Schema(query = Query, mutation=Mutation)


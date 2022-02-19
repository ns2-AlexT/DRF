Добрый день!

Поправил код вызываемый при переопределении метода 'destroy' в контроллере 'ToDoNoteModelViewSet'

Задания 4 лекции:
  1 - Выполнено.
  2 - Выполнено.
  3 -   для модели User, Project: реализовано с помощью класса ViewSet
        для модели ToDoNote: реализовано с помощью класса APIView
  4 - Выполнено, пришлось закомментировать строки:
            # name_of_project = serializers.StringRelatedField()
  5 - Выполнено, добавил отображение заметок для конкретного проекта.

  Так и не смог устранить ошибку:  Uncaught TypeError: note.name_of_project.includes is not a function
  Подскажите в чем моя ошибка, пожалуйста.

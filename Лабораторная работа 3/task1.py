class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Book" (базовый класс)
        :param name: Название
        :param author: Автор
        """
        self._name = name
        self._author = author

    @property  # Так как атрибут name изменять пользователю нельзя, пишем для него свойство getter
    def name(self) -> str:
        return self._name

    @property  # Так как атрибут author изменять пользователю нельзя, пишем для него свойство getter
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        """
        Метод __str__ должен возвращать строку формата, где "название_книги" берется с помощью атрибута name,
        а "автор_книги" берется с помощью атрибута author
        :return: Книга "название_книги". Автор "автор_книги"
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        """
        Метод __repr__ должен возвращать валидную python строку,
        по которой можно инициализировать точно такой же экземпляр
        :return: Book(name='_', author='_')
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "PaperBook" (дочерний класс)
        :param name: Название
        :param author: Автор
        :param pages: Количество страниц
        """
        super().__init__(name, author)  # Атрибуты name и author наследуются из базового класса
        self.pages = pages

    @property  # Свойство setter может существовать только совместно с getter
    def pages(self) -> int:
        return self._pages

    @pages.setter  # В свойстве setter можно организовать проверку принимаемого значения
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
        self._pages = pages

    def __str__(self) -> str:
        """
        Метод __str__ должен возвращать строку формата, где "название_книги" берется с помощью атрибута name,
        "автор_книги" берется с помощью атрибута author, "количество_страниц" берется с помощью атрибута pages
        :return: Книга "название_книги". Автор "автор_книги". Количество страниц "количество_страниц"
        """
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"
        # Если нет необходимости указывать тип книги и количество страниц, то метод можно наследовать из базового класса

    def __repr__(self) -> str:
        """
        Метод __repr__ должен возвращать валидную python строку,
        по которой можно инициализировать точно такой же экземпляр
        :return: PaperBook(name='_', author='_', pages=_)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"
        # Если нет необходимости указывать количество страниц, то метод можно наследовать из базового класса


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе объекта "AudioBook" (дочерний класс)
        :param name: Название
        :param author: Автор
        :param duration: Продолжительность
        """
        super().__init__(name, author)  # Атрибуты name и author наследуются из базового класса
        self.duration = duration

    @property  # Свойство setter может существовать только совместно с getter
    def duration(self) -> float:
        return self._duration

    @duration.setter  # В свойстве setter можно организовать проверку принимаемого значения
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise ValueError
        self._duration = duration

    def __str__(self) -> str:
        """
        Метод __str__ должен возвращать строку формата, где "название_книги" берется с помощью атрибута name,
        "автор_книги" берется с помощью атрибута author, "продолжительность" берется с помощью атрибута duration
        :return: Книга "название_книги". Автор "автор_книги". Продолжительность "продолжительность"
        """
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность {self.duration}"
        # Если нет необходимости указывать тип книги и продолжительность, то метод можно наследовать из базового класса

    def __repr__(self) -> str:
        """
        Метод __repr__ должен возвращать валидную python строку,
        по которой можно инициализировать точно такой же экземпляр
        :return: AudioBook(name='_', author='_', duration=_)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
        # Если нет необходимости указывать продолжительность, то метод можно наследовать из базового класса

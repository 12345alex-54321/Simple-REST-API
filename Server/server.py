from fastapi import FastAPI, Response, status
from pydantic import BaseModel, Field
import uvicorn
import asyncio

class ExpertModel:

    def __init__(self):

        self.Knowledge_Base = [
            {
                "Вопрос" : "Тип Отдыха",
                "Ответ" : [
                "Пляжный", 
                "Культурный", 
                "Активный", 
                "Гастрономический", 
                "Экотуризм", 
                "Оздоровительный / SPA", 
                "Горнолыжный"
                ]
            },
            {
                "Вопрос" : "Климат",
                "Ответ" : [
                    "Жаркий", 
                    "Средний", 
                    "Прохладный", 
                    "Экстремальный / Арктический"
                ]
            },
            {
                "Вопрос" :"Бюджет",
                "Ответ" : [
                    "Низкий", 
                    "Средний", 
                    "Высокий", 
                    "Премиум / Люкс"
                ]
            },
            
            {
                "Вопрос" : "Компания",
                "Ответ" : [
                    "Один", 
                    "Парой", 
                    "С детьми", 
                    "С друзьями", 
                    "Большой семейный круг"
                ]
            },
            {
                "Вопрос" : "Сезон",
                "Ответ" : [
                    "Лето", 
                    "Зима", 
                    "Межсезонье",
                    "Круглый год"
                ]
            },
            {
                "Вопрос" : "Локация",
                "Ответ" : [
                    "Внутри страны", 
                    "За рубежом"
                ]
            }
        ]

        self.Destinations = [
            {
                "Название": "Мальдивы",
                "Профиль": 
                {
                    "Тип Отдыха": 0, 
                    "Климат": 0, 
                    "Бюджет": 3, 
                    "Компания": 1, 
                    "Сезон": 3, 
                    "Локация": 1
                }
            },
            {
                "Название": "Алтай (Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 4, 
                    "Климат": 1, 
                    "Бюджет": 1, 
                    "Компания": 3, 
                    "Сезон": 0, 
                    "Локация": 0
                }
            },
            {
                "Название": "Рим (Италия)",
                "Профиль": 
                {
                    "Тип Отдыха": 1, 
                    "Климат": 1, 
                    "Бюджет": 2, 
                    "Компания": 1, 
                    "Сезон": 2, 
                    "Локация": 1
                }
            },
            {
                "Название": "Сочи (Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 0, 
                    "Климат": 0, 
                    "Бюджет": 1, 
                    "Компания": 2, 
                    "Сезон": 0, 
                    "Локация": 0
                }
            },
            {
                "Название": "Шерегеш (Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 6, 
                    "Климат": 2, 
                    "Бюджет": 1, 
                    "Компания": 3, 
                    "Сезон": 1, 
                    "Локация": 0
                }
            },
            {
                "Название": "Париж (Франция)",
                "Профиль": 
                {
                    "Тип Отдыха": 1, 
                    "Климат": 1, 
                    "Бюджет": 2, 
                    "Компания": 1, 
                    "Сезон": 2, 
                    "Локация": 1
                }
            },
            {
                "Название": "Кавказские Минеральные Воды (Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 5, 
                    "Климат": 1, 
                    "Бюджет": 0, 
                    "Компания": 4, 
                    "Сезон": 3, 
                    "Локация": 0
                }
            },
            {
                "Название": "Бангкок (Таиланд)",
                "Профиль": 
                {
                    "Тип Отдыха": 3, 
                    "Климат": 0, 
                    "Бюджет": 1, 
                    "Компания": 3, 
                    "Сезон": 1, 
                    "Локация": 1
                }
            },
            {
                "Название": "Карелия (Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 4, 
                    "Климат": 2, 
                    "Бюджет": 0, 
                    "Компания": 2, 
                    "Сезон": 0, 
                    "Локация": 0
                }
            },
            {
                "Название": "Дубай (ОАЭ)",
                "Профиль": 
                {
                    "Тип Отдыха": 0, 
                    "Климат": 0, 
                    "Бюджет": 3, 
                    "Компания": 2, 
                    "Сезон": 1, 
                    "Локация": 1
                }
            },
            {
                "Название": "Куршевель (Франция)",
                "Профиль": 
                {
                    "Тип Отдыха": 6, 
                    "Климат": 2, 
                    "Бюджет": 3, 
                    "Компания": 1, 
                    "Сезон": 1, 
                    "Локация": 1
                }
            },
            {
                "Название": "Мурманск (Териберка, Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 2, 
                    "Климат": 3, 
                    "Бюджет": 1, 
                    "Компания": 0, 
                    "Сезон": 1, 
                    "Локация": 0
                }
            },
            {
                "Название": "Токио (Япония)",
                "Профиль": 
                {
                    "Тип Отдыха": 1, 
                    "Климат": 1, 
                    "Бюджет": 3, 
                    "Компания": 0, 
                    "Сезон": 2, 
                    "Локация": 1
                }
            },
            {
                "Название": "Камчатка (Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 2, 
                    "Климат": 2, 
                    "Бюджет": 2, 
                    "Компания": 3, 
                    "Сезон": 0, 
                    "Локация": 0
                }
            },
            {
                "Название": "Стамбул (Турция)",
                "Профиль": 
                {
                    "Тип Отдыха": 3, 
                    "Климат": 1, 
                    "Бюджет": 1, 
                    "Компания": 1, 
                    "Сезон": 2, 
                    "Локация": 1
                }
            },
            {
                "Название": "Байкал (Листвянка, Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 4, 
                    "Климат": 2, 
                    "Бюджет": 1, 
                    "Компания": 4, 
                    "Сезон": 1, 
                    "Локация": 0
                }
            },
            {
                "Название": "Бали (Индонезия)",
                "Профиль": 
                {
                    "Тип Отдыха": 0, 
                    "Климат": 0, 
                    "Бюджет": 2, 
                    "Компания": 1, 
                    "Сезон": 3, 
                    "Локация": 1
                }
            },
            {
                "Название": "Санкт-Петербург (Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 1, 
                    "Климат": 1, 
                    "Бюджет": 1, 
                    "Компания": 2, 
                    "Сезон": 0, 
                    "Локация": 0
                }
            },
            {
                "Название": "Исландия (Рейкьявик)",
                "Профиль": 
                {
                    "Тип Отдыха": 2, 
                    "Климат": 2, 
                    "Бюджет": 3, 
                    "Компания": 0, 
                    "Сезон": 0, 
                    "Локация": 1
                }
            },
            {
                "Название": "Красная Поляна (Роза Хутор, Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 6, 
                    "Climate": 1, 
                    "Бюджет": 2, 
                    "Компания": 3, 
                    "Сезон": 1, 
                    "Локация": 0
                }
            },
            {
                "Название": "Грузия (Тбилиси / Боржоми)",
                "Профиль": 
                {
                    "Тип Отдыха": 3, 
                    "Климат": 1, 
                    "Бюджет": 0, 
                    "Компания": 3, 
                    "Сезон": 2, 
                    "Локация": 1
                }
            },
            {
                "Название": "Дагестан (Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 2, 
                    "Климат": 0, 
                    "Бюджет": 0, 
                    "Компания": 3, 
                    "Сезон": 0, 
                    "Локация": 0
                }
            },
            {
                "Название": "Баден-Баден (Германия)",
                "Профиль": 
                {
                    "Тип Отдыха": 5, 
                    "Климат": 1, 
                    "Бюджет": 3, 
                    "Компания": 1, 
                    "Сезон": 3, 
                    "Локация": 1
                }
            },
            {
                "Название": "Белокуриха (Россия)",
                "Профиль": 
                {
                    "Тип Отдыха": 5, 
                    "Климат": 1, 
                    "Бюджет": 1, 
                    "Компания": 2, 
                    "Сезон": 2, 
                    "Локация": 0
                }
            }
        ]

    def FindBestDestination(self, user_answer: dict):
        scored_destinations = []
        answers = user_answer.model_dump(by_alias=True)
        for dest in self.Destinations:
            score = 0
            for criterion, user_value in answers.items():
                if criterion in dest["Профиль"] and dest["Профиль"][criterion] == user_value:
                    score += 1
            scored_destinations.append((dest, score))
            scored_destinations.sort(key=lambda x: x[1], reverse=True)
        max_scores = max(dest[1] for dest in scored_destinations)
        current_dest = [dest[0] for dest in scored_destinations if dest[1] == max_scores]
        if(len(current_dest) > 3):
            current_dest = current_dest[0:3]
        return current_dest

class Answer(BaseModel):

    VacationType: int = Field(alias = "Тип Отдыха", ge = 0, le = 6)
    Climat: int = Field(alias = "Климат", ge = 0, le = 3)
    Budget: int = Field(alias = "Бюджет", ge = 0, le = 3)
    Company: int = Field(alias = "Компания", ge = 0, le = 4)
    Season: int = Field(alias = "Сезон", ge = 0, le = 3)
    Location: int = Field(alias = "Локация", ge = 0, le = 1)

class Api_Service:

    def __init__(self, addr: str, p: int = 8000):

        self.app = FastAPI()
        self.model = ExpertModel()

        self.address = addr
        self.port = p

        self._register_routes()

        self._server: uvicorn.Server | None = None
        
    def _register_routes(self):

        self.app.add_api_route("/questions/{question_id}", self.ask_question, methods=["GET"])
        self.app.add_api_route("/answers/", self.create_answer, methods=["POST"])

    async def ask_question(self, question_id: int, response: Response):

        if(question_id >= 0 and question_id < len(self.model.Knowledge_Base)):
            response.status_code = status.HTTP_200_OK
            server_answer = self.model.Knowledge_Base[question_id]
            server_answer["total"] = len(self.model.Knowledge_Base)
            return server_answer
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"total" : len(self.model.Knowledge_Base), "message" : "KeyError"}
        
    async def create_answer(self, user_answer: Answer):
        destiantions = self.model.FindBestDestination(user_answer)
        return destiantions

    async def StartServer(self):
        print("Starting server....")

        config = uvicorn.Config(
            app = self.app,
            host=self.address,
            port=self.port,
            log_level="info"
        )

        self._server = uvicorn.Server(config)
        await self._server.serve()


    def StopServer(self):
        if self._server is not None:
            self._server.should_exit = True



Раздел “О нас”

№1. Иконка стрелки отображается не полностью на всех экранах

Описание:
Во всех разделах приложения, где используется иконка стрелки (например, кнопки “назад”, “вперёд”, переход в другой раздел и т.д.), иконка отображается не полностью. Проблема наблюдается во всех подобных элементах — стрелка частично обрезана.

Шаги для воспроизведения:
1.	Открыть страницу “О нас”.
2.	Прокрутить до блока “V.A. Group в цифрах”.
3.	Прокрутить до конца страницы до элемента “Next V.A. CRM”.
4.	Посмотреть на отображение стрелки.

Ожидаемый результат:
Иконка стрелки должна быть полностью видимой и корректно отображаться во всех разделах.

Фактический результат:
Иконка отображается частично — отсутствует часть стрелки.


Окружение:
•	Устройство: MacBook Air
•	Браузер: Google Chrome


Attachments: bug№1About ,  bug№1.About

Доп. информация:
•	Возможная причина: CSS-свойства (overflow: hidden, padding, margin)

⸻

№2. Пагинация работает некорректно: при нажатии “вперёд” открывается предыдущая страница и наоборот

Описание:
В разделе A.V. Group CRM наблюдается некорректное поведение пагинации. При попытке перейти на следующую страницу загружается предыдущая, и наоборот.

Шаги для воспроизведения:
1.	Перейти в раздел A.V. Group CRM, блок “V.A. Group в цифрах”.
2.	Нажать на переход к следующей странице.
3.	Обратить внимание, что загружается предыдущая.
4.	Повторить переход назад — загружается следующая страница.

Ожидаемый результат:
•	«Вперёд» открывает следующую страницу.
•	«Назад» возвращает на предыдущую.

Фактический результат:
•	При нажатии «вперёд» — загружается предыдущая.
•	При нажатии «назад» — загружается следующая.

Окружение:
•	Устройство: MacBook Air
•	Браузер: Google Chrome

Attachments:
Видео: bug№2About


**№3 При пагинации в верхней части страницы остаётся видимым обрезанный фрагмент текста**

**Описание:**

В разделе **О нас**, при переключении страниц с помощью пагинации, в верхней части блока остаётся обрезанный кусочек текста, относящийся к тексту “V.A. Group в цифрах”. Это визуально выглядит нормально, но желательно что бы этого кусочка не было видно

---

**Шаги для воспроизведения:**

1.	Перейти в раздел **О нас**, где реализована пагинация.

2.	Пролистать до блока V.A. Group в цифрах.

3.	Нажать на элемент пагинации для перехода на другую страницу.

4.	Обратить внимание на верхнюю часть блока после загрузки.

---

**Фактический результат:**

– В верхней части экрана остаётся обрезанный фрагмент текста.

– Визуально мешает восприятию основного контента.

**Ожидаемый результат:**

– После перехода на другую страницу отображение должно начинаться с чистого контента новой страницы.

– Не должно быть визуальных “остатков”.

---

**Окружение:**

Устройство: MacBook Air

Браузер: Google Chrome

**Attachments:**

–Видео: bug№3AboutV, bug№3AboutImg

⸻

Раздел “V.A. CRM”

№1. Фигура круга перекрывает текст при скроллинге

Описание:
При прокрутке страницы декоративная круглая фигура смещается поверх текстов и перекрывает содержимое. Проблема проявляется в разделах:
•	V.A. CRM
•	Бизнес аналитика и консалтинг
•	V.A. Apps
•	Affiliate Marketing

Шаги для воспроизведения:
1.	Перейти в любой из указанных разделов.
2.	Прокрутить страницу вниз.
3.	Посмотреть на перекрытие текста фигурой.

Ожидаемый результат:
Текст должен быть полностью видим и не перекрываться фигурами.

Фактический результат:
Фигура перекрывает заголовки и основной текст.

Окружение:
•	Устройство: MacBook Air
•	Браузер: Google Chrome

Attachments:
Видео: bug№1CRM

⸻

№2. Скачок страницы вверх при вводе текста в форму и некорректная подсветка поля

Описание:
При вводе текста в форму заявки:
•	Страница автоматически прокручивается вверх, теряя фокус на форме.
•	После ввода фон поля становится белым, нарушая дизайн.

Шаги для воспроизведения:
1.	Перейти в A.V. Group CRM.
2.	Открыть форму заявки.
3.	Начать ввод текста в любое текстовое поле.
4.	Отследить автоскролл и изменение фона.

Ожидаемый результат:
•	Страница не должна прыгать вверх.
•	Стиль поля должен оставаться корректным.

Фактический результат:
•	Скролл уходит вверх.
•	Цвет поля меняется на белый.

Окружение:
•	Устройство: MacBook Air
•	Браузер: Google Chrome

Attachments:
Видео: bug№2CRM

⸻

№3. Поля формы заявки позволяют вводить некорректные данные

Описание:
•	Поле “Имя” принимает цифры.
•	Поле “Номер телефона” принимает буквы.
•	Форма успешно отправляется даже с ошибками.

Шаги для воспроизведения:
1.	Перейти в форму A.V. Group CRM.
2.	Ввести:
•	В “Имя” — 12345
•	В “Телефон” — abc123
3.	Заполнить остальные поля.
4.	Отправить форму.

Ожидаемый результат:
•	Имя: только буквы.
•	Телефон: только цифры.
•	При ошибке — запрет на отправку.

Фактический результат:
•	Ошибки не появляются.
•	Форма отправляется.
•	Появляется сообщение об успехе.

Окружение:
•	Устройство: MacBook Air
•	Браузер: Google Chrome

Attachments:
Фото: bug№3CRM

⸻

№4. Некорректный скролл при вводе текста в поле “Расскажи о своём опыте”

Описание:
При вводе большого текста (1600 символов) происходит прокрутка всей страницы, а не только текстового поля. Пользователь теряет контекст.

Шаги для воспроизведения:
1.	Перейти в раздел A.V. Group CRM.
2.	Найти поле “Расскажи о своём опыте”.
3.	Ввести большой текст.
4.	Посмотреть поведение прокрутки.

Ожидаемый результат:
•	Прокручивается только текстовое поле.

Фактический результат:
•	Прокручивается вся страница, уводя форму из зоны видимости.

Окружение:
•	Устройство: MacBook Air
•	Браузер: Google Chrome

Attachments:
Видео: bug№4CRM

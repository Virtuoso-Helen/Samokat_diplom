[![Typing SVG](https://readme-typing-svg.demolab.com?font=arial+black&size=30&duration=2000&pause=1000&color=5DA7F7&multiline=true&random=true&width=460&lines=%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F+%D1%82%D0%B5%D1%81%D1%82%D0%B0+%D0%BA+API)](https://git.io/typing-svg)

Автоматизируем сценарий, который подготовили коллеги-тестировщики:
1. [x] Клиент создает заказ.
2. [x] Проверяется, что по треку заказа можно получить данные о заказе.

## **Шаги**

1. [x] Выполнить запрос на создание заказа.
2. [x] Сохранить номер трека заказа.
3. [x] Выполнить запрос на получения заказа по треку заказа.
4. [x] Проверить, что код ответа равен 200.



<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=arial+black&size=30&duration=2000&pause=1000&color=5DA7F7&multiline=true&random=true&width=460&lines=%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0+%D1%81+%D0%B1%D0%B0%D0%B7%D0%BE%D0%B9+%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85" alt="Typing SVG" /></a>

## **Задание 1**

Нужно проверить, отображается ли созданный заказ в базе данных.     
Для этого: Необходимо вывести список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

**Ответ:**


    SELECT track AS TrackID,
        CASE 
         WHEN finished = true THEN 2 
         WHEN cancelled = true THEN -1 
         WHEN "inDelivery" = true THEN 1 
         ELSE 0 
        END AS Status 
    FROM "Orders";


##**Задание 2**

Тестируем статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выводим все трекеры заказов и их статусы.

Статусы определяются по следующему правилу:

Если поле finished == true, то вывести статус 2.    
Если поле canсelled == true, то вывести статус -1.  
Если поле inDelivery == true, то вывести статус 1.  
Для остальных случаев вывести 0.    
Технические примечания:     
У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.

**Ответ:**

    SELECT c.login, COUNT(o.track) AS "inDeliveryCount" 
    FROM "Couriers" AS c 
    LEFT JOIN "Orders" AS o ON c.id = o."courierId" 
    WHERE o."inDelivery" = true 
    GROUP BY c.login;

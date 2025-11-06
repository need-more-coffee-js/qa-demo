-- Создание таблицы
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INT
);

-- Выбор всех сотрудников
SELECT * FROM employees;

-- Подсчёт количества сотрудников по отделам
SELECT department, COUNT(*) FROM employees GROUP BY department;

-- Выбор сотрудников с зарплатой выше 100000
SELECT * FROM employees WHERE salary > 100000;

-- Сортировка по зарплате
SELECT * FROM employees ORDER BY salary DESC;

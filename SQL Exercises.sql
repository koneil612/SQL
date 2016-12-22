-- -- -- Give the number of employees that live in TX
-- SELECT count(*) from address
-- WHERE state= "TX";

-- List the average income of employee by state
-- select AVG (income), state from address_employee
-- left JOIN income on address_employee.employee_id = income.id 
-- left join address on address_employee.address_id = address.id
-- Group by (state);

-- -- -- List the employee(s) with the highest income
-- select income, firstname, lastname from income
-- left JOIN employee on employee.id =income.employee_id
-- Group by (income) desc limit 1
-- 

-- ------ Add a second address for all employees that make over 220K (it's ok to use the same value for their primary address)
-- insert into address (line1, city, state, zip) select line1, city, state, zip from address
-- -- select employee_id, firstname from employee
-- left join address_employee on address.id=address_employee.address_id
-- left join income on address_employee.employee_id=income.id
-- where income >220000
-- insert into address_employee(address_id, employee_id) select a1.id,ae.employee_id 
-- from address a1
-- inner join address a2 on a1.line1 = a2.line1 and a1.city=a2.city and a1.id<>a2.id
-- inner join address_employee ae on a2.id=ae.address_id



-- ------Give everyone a 10% raise
-- update income
-- set income.income = (income * 1.10) 
-- where id > 0 

-- -- --- -- Give all employee(s) that makes the lowest amount a 5000 raise
-- select income, firstname, lastname, employee_id from income
-- left JOIN employee on employee.id =income.employee_id
-- Group by (income) asc limit 1
-- 
update income
set income.income = (income + 5000) 
having MIN(icome) 

-- -- -- Delete any employee whose last name starts with a W

-- select SUM(income) from income;


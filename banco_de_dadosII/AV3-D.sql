SELECT employees.first_name, employees.last_name, departments.dept_name
	FROM (dept_emp join departments on dept_emp.dept_no=departments.dept_no)
		join employees on employees.emp_no=dept_emp.emp_no;
		
SELECT employees.first_name, employees.last_name, departments.dept_name 
	FROM employees,departments, dept_emp
	WHERE employees.emp_no=dept_emp.emp_no and dept_emp.dept_no=department.dept_no;

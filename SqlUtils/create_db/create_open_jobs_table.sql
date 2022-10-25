USE res_alert;
CREATE TABLE open_jobs(
    oj_id INT PRIMARY KEY,
    job_name VARCHAR(255),
    department_name VARCHAR(255),

    FOREIGN KEY(department_name) REFERENCES departements(dep_name)
);
USE res_alert;
CREATE TABLE departements(
    dep_name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE final_stage(
    fs_name VARCHAR(255) NOT NULL PRIMARY KEY
);

CREATE TABLE status(
    s_order INT, 
    s_name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE candidates(
    c_first_name VARCHAR(255),
    c_last_name VARCHAR(255),
    c_mail VARCHAR(255) PRIMARY KEY,
    c_cv VARCHAR(255),
    c_gender VARCHAR(255)
);


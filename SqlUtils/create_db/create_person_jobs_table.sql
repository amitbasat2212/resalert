USE res_alert;
CREATE TABLE person_jobs(
    candidante_id VARCHAR(255),
    job_id INT,
    status VARCHAR(255),
    final_stage VARCHAR(255),
    PRIMARY KEY (candidante_id, job_id),

    FOREIGN KEY(candidante_id) REFERENCES candidates(c_mail),
    FOREIGN KEY(job_id) REFERENCES open_jobs(oj_id),
    FOREIGN KEY(status) REFERENCES status(s_name),
    FOREIGN KEY(final_stage) REFERENCES final_stage(fs_name)
);
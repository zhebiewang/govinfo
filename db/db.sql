
DROP TABLE phfee;
CREATE TABLE phfee
    (
        title VARCHAR(1000),
        url VARCHAR(1000),
        update_dt DATE,
        content VARCHAR(10000),
        taxonmoy VARCHAR(10),
       	region VARCHAR(10),
        loadts TIMESTAMP default CURRENT_TIMESTAMP
       	
    );
;


DROP TABLE taxonmoy;
CREATE TABLE taxonmoy
	(
		tax_id INT KEY NOT NULL AUTO_INCREMENT,
		tax_cd VARCHAR(10),
		tax_term VARCHAR(20),
		tex_description VARCHAR(1000)
	);
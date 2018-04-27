DROP TABLE IF EXISTS USER CASCADE;
DROP TABLE IF EXISTS USER_EVENT CASCADE;
DROP TABLE IF EXISTS USER_ASSOCIATION CASCADE;
DROP TABLE IF EXISTS ASSOCIATION CASCADE;
DROP TABLE IF EXISTS EVENT CASCADE;

CREATE TABLE USER(
    email             VARCHAR(64)     NOT NULL DEFAULT '',
    email_ticket      VARCHAR(64),
    password          VARCHAR(64)     NOT NULL DEFAULT '',
    login             VARCHAR(64),                
    firstname         VARCHAR(64)     NOT NULL DEFAULT '',
    lastname          VARCHAR(64)     NOT NULL DEFAULT '',
    student           BOOLEAN,
    access_level      INTEGER         NOT NULL DEFAULT 0,

    PRIMARY KEY(email)
);

CREATE TABLE USER_EVENT(
    id                SERIAL          NOT NULL,
    billet_type       INTEGER         NOT NULL,
    inside            BOOLEAN         NOT NULL,
    staff             BOOLEAN         NOT NULL DEFAULT FALSE,
    user_id           INTEGER         NOT NULL DEFAULT O,
    event_id          INTEGER         NOT NULL DEFAULT O,

    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES USER,
    FOREIGN KEY(event_id) REFERENCES EVENT
);

CREATE TABLE USER_ASSOCIATION(
    id                SERIAL          NOT NULL,
    members_mail      VARCHAR(64)     NOT NULL DEFAULT '',
    association_name  VARCHAR(64)     NOT NULL DEFAULT '',

    PRIMARY KEY (id),
    FOREIGN KEY(members_mail) REFERENCES USER,
    FOREIGN KEY(association_name) REFERENCES ASSOCIATION
);

CREATE TABLE ASSOCIATION(
    name              VARCHAR(64)     NOT NULL,
    uri               VARCHAR(64)     NOT NULL,

    PRIMARY KEY(id)
);

CREATE TABLE EVENT(
    title             VARCHAR(64)     NOT NULL,
    description       VARCHAR(64),
    start_date        DATE            NOT NULL,
    end_date          DATE            NOT NULL,
    end_inscrip_date  DATE            NOT NULL,
    max_place_stud    INTEGER         NOT NULL,
    max_place_ext     INTEGER         NOT NULL,
    price_student     INTEGER         NOT NULL,
    price_extern      INTEGER         NOT NULL,
    display_available_places BOOLEAN  NOT NULL,
    status            INTEGER         NOT NULL,
    premium           BOOLEAN         NOT NULL,
    nb_registered     INTEGER         NOT NULL,
    nb_registered_used    INTEGER     NOT NULL,
    nb_registered_inside  INTEGER     NOT NULL,

    PRIMARY KEY (title),
);

DROP TABLE IF EXISTS USER CASCADE;
DROP TABLE IF EXISTS USER_EVENT CASCADE;
DROP TABLE IF EXISTS USER_ASSOCIATION CASCADE;
DROP TABLE IF EXISTS ASSOCIATION CASCADE;
DROP TABLE IF EXISTS EVENT CASCADE;

CREATE TABLE USER(
    email           VARCHAR(64)     NOT NULL DEFAULT '',
    email_ticket    VARCHAR(64)
    password        VARCHAR(64)     NOT NULL DEFAULT '',
    login           VARCHAR(64),                
    firstname       VARCHAR(64)     NOT NULL DEFAULT '',
    lastname        VARCHAR(64)     NOT NULL DEFAULT '',
    student         BOOLEAN
    access_level    INTEGER         NOT NULL DEFAULT 0,
    ;

CREATE TABLE USER_EVENT(
    name        VARCHAR(64)     NOT NULL DEFAULT '',
    
    PRIMARY KEY (name),
    UNIQUE(name)
);

CREATE TABLE USER_ASSOCIATION(
    id          SERIAL          NOT NULL,
    title       VARCHAR(64)     NOT NULL DEFAULT '',
    artist      VARCHAR(64)     NOT NULL DEFAULT '',
    duration    INT             NOT NULL DEFAULT 0,

    PRIMARY KEY (id),
    UNIQUE(title, artist)
);

CREATE TABLE ASSOCIATION(
    id          SERIAL NOT NULL,
    song_id     SERIAL NOT NULL,
    album       VARCHAR(64) NOT NULL DEFAULT '',
    artist      VARCHAR(64) NOT NULL DEFAULT '',
    track       INT NOT NULL DEFAULT 0,

    PRIMARY KEY (id),
    FOREIGN KEY (song_id) REFERENCES song(id),
    UNIQUE (album, track),
    CHECK (track > 0)
);

CREATE TABLE EVENT(
    email       VARCHAR(64)     NOT NULL DEFAULT '',
    name        VARCHAR(64)     NOT NULL DEFAULT '',

    PRIMARY KEY (email),
    UNIQUE (email)
);

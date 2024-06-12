--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin (
    id integer NOT NULL,
    firstname character varying(45),
    lastname character varying(45),
    middlename character varying(45),
    email character varying(45),
    mobile character varying(45),
    date_registered date
);


ALTER TABLE public.admin OWNER TO postgres;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    id integer NOT NULL,
    name character varying(45) NOT NULL
);


ALTER TABLE public.category OWNER TO postgres;

--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO postgres;

--
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;


--
-- Name: complainant; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.complainant (
    id integer NOT NULL,
    firstname character varying(45),
    lastname character varying(45),
    middlename character varying(45),
    email character varying(45),
    mobile character varying(20),
    address character varying(100),
    zipcode integer,
    status character varying(45),
    date_registered date
);


ALTER TABLE public.complainant OWNER TO postgres;

--
-- Name: complaint; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.complaint (
    id integer NOT NULL,
    cid integer NOT NULL,
    catid integer NOT NULL,
    ctype integer NOT NULL
);


ALTER TABLE public.complaint OWNER TO postgres;

--
-- Name: complaint_details; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.complaint_details (
    id integer NOT NULL,
    compid integer NOT NULL,
    statement character varying(100) NOT NULL,
    status character varying(50),
    resolution character varying(100),
    date_resolved date
);


ALTER TABLE public.complaint_details OWNER TO postgres;

--
-- Name: complaint_details_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.complaint_details_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.complaint_details_id_seq OWNER TO postgres;

--
-- Name: complaint_details_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.complaint_details_id_seq OWNED BY public.complaint_details.id;


--
-- Name: complaint_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.complaint_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.complaint_id_seq OWNER TO postgres;

--
-- Name: complaint_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.complaint_id_seq OWNED BY public.complaint.id;


--
-- Name: complaint_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.complaint_type (
    id integer NOT NULL,
    name character varying(45) NOT NULL
);


ALTER TABLE public.complaint_type OWNER TO postgres;

--
-- Name: complaint_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.complaint_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.complaint_type_id_seq OWNER TO postgres;

--
-- Name: complaint_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.complaint_type_id_seq OWNED BY public.complaint_type.id;


--
-- Name: login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login (
    id integer NOT NULL,
    username character varying(45),
    password character varying(45),
    user_type integer
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: login_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.login_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.login_id_seq OWNER TO postgres;

--
-- Name: login_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.login_id_seq OWNED BY public.login.id;


--
-- Name: category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);


--
-- Name: complaint id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint ALTER COLUMN id SET DEFAULT nextval('public.complaint_id_seq'::regclass);


--
-- Name: complaint_details id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_details ALTER COLUMN id SET DEFAULT nextval('public.complaint_details_id_seq'::regclass);


--
-- Name: complaint_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_type ALTER COLUMN id SET DEFAULT nextval('public.complaint_type_id_seq'::regclass);


--
-- Name: login id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login ALTER COLUMN id SET DEFAULT nextval('public.login_id_seq'::regclass);


--
-- Data for Name: admin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.admin (id, firstname, lastname, middlename, email, mobile, date_registered) FROM stdin;
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
9eafa601a7db
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (id, name) FROM stdin;
\.


--
-- Data for Name: complainant; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.complainant (id, firstname, lastname, middlename, email, mobile, address, zipcode, status, date_registered) FROM stdin;
\.


--
-- Data for Name: complaint; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.complaint (id, cid, catid, ctype) FROM stdin;
\.


--
-- Data for Name: complaint_details; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.complaint_details (id, compid, statement, status, resolution, date_resolved) FROM stdin;
\.


--
-- Data for Name: complaint_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.complaint_type (id, name) FROM stdin;
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, username, password, user_type) FROM stdin;
1	admin	admin2255	1
2	sjctrags	sjctrags2255	2
3	olaola	olaola2255	1
4	alibatasys	alibatasys	1
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_id_seq', 1, false);


--
-- Name: complaint_details_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.complaint_details_id_seq', 1, false);


--
-- Name: complaint_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.complaint_id_seq', 1, false);


--
-- Name: complaint_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.complaint_type_id_seq', 1, false);


--
-- Name: login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_id_seq', 4, true);


--
-- Name: admin admin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- Name: complainant complainant_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complainant
    ADD CONSTRAINT complainant_pkey PRIMARY KEY (id);


--
-- Name: complaint_details complaint_details_compid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_details
    ADD CONSTRAINT complaint_details_compid_key UNIQUE (compid);


--
-- Name: complaint_details complaint_details_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_details
    ADD CONSTRAINT complaint_details_pkey PRIMARY KEY (id);


--
-- Name: complaint complaint_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint
    ADD CONSTRAINT complaint_pkey PRIMARY KEY (id);


--
-- Name: complaint_type complaint_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_type
    ADD CONSTRAINT complaint_type_pkey PRIMARY KEY (id);


--
-- Name: login login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_pkey PRIMARY KEY (id);


--
-- Name: admin admin_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_id_fkey FOREIGN KEY (id) REFERENCES public.login(id);


--
-- Name: complainant complainant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complainant
    ADD CONSTRAINT complainant_id_fkey FOREIGN KEY (id) REFERENCES public.login(id);


--
-- Name: complaint complaint_catid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint
    ADD CONSTRAINT complaint_catid_fkey FOREIGN KEY (catid) REFERENCES public.category(id);


--
-- Name: complaint complaint_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint
    ADD CONSTRAINT complaint_cid_fkey FOREIGN KEY (cid) REFERENCES public.complainant(id);


--
-- Name: complaint complaint_ctype_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint
    ADD CONSTRAINT complaint_ctype_fkey FOREIGN KEY (ctype) REFERENCES public.complaint_type(id);


--
-- Name: complaint_details complaint_details_compid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.complaint_details
    ADD CONSTRAINT complaint_details_compid_fkey FOREIGN KEY (compid) REFERENCES public.complaint(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


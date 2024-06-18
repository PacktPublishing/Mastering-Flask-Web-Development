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

--
-- Name: administrator_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.administrator_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administrator_id_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: administrator; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.administrator (
    id bigint DEFAULT nextval('public.administrator_id_seq'::regclass) NOT NULL,
    empid character varying(25) NOT NULL,
    username_id character varying(50) NOT NULL,
    firstname character varying(100) NOT NULL,
    lastname character varying(100) NOT NULL,
    "position" character varying(100) NOT NULL,
    email character varying(20) NOT NULL,
    mobile character varying(20) NOT NULL,
    issued_date date NOT NULL
);


ALTER TABLE public.administrator OWNER TO postgres;

--
-- Name: book_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.book_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.book_id_seq OWNER TO postgres;

--
-- Name: book; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.book (
    id bigint DEFAULT nextval('public.book_id_seq'::regclass) NOT NULL,
    code character varying(20) NOT NULL,
    title character varying(100) NOT NULL,
    author character varying(100) NOT NULL,
    isbn character varying(100) NOT NULL,
    published_year integer NOT NULL,
    edition integer NOT NULL,
    publisher_id character varying(20) NOT NULL,
    category_id character varying(20) NOT NULL,
    description character varying(200) NOT NULL
);


ALTER TABLE public.book OWNER TO postgres;

--
-- Name: borrow_faculty_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.borrow_faculty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.borrow_faculty_id_seq OWNER TO postgres;

--
-- Name: borrow_faculty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.borrow_faculty (
    id bigint DEFAULT nextval('public.borrow_faculty_id_seq'::regclass) NOT NULL,
    bookcode_id character varying(20) NOT NULL,
    empid_id character varying(25) NOT NULL,
    borrowed_date date NOT NULL,
    returned_date date NOT NULL,
    duration integer NOT NULL,
    approved_by character varying(100) NOT NULL
);


ALTER TABLE public.borrow_faculty OWNER TO postgres;

--
-- Name: borrow_student_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.borrow_student_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.borrow_student_id_seq OWNER TO postgres;

--
-- Name: borrow_student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.borrow_student (
    id bigint DEFAULT nextval('public.borrow_student_id_seq'::regclass) NOT NULL,
    bookcode_id character varying(20) NOT NULL,
    studid_id character varying(25) NOT NULL,
    borrowed_date date NOT NULL,
    duration integer NOT NULL,
    returned_date date NOT NULL,
    approved_by character varying(100) NOT NULL
);


ALTER TABLE public.borrow_student OWNER TO postgres;

--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO postgres;

--
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    id bigint DEFAULT nextval('public.category_id_seq'::regclass) NOT NULL,
    code character varying(20) NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(200) NOT NULL
);


ALTER TABLE public.category OWNER TO postgres;

--
-- Name: faculty_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faculty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faculty_id_seq OWNER TO postgres;

--
-- Name: faculty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faculty (
    id bigint DEFAULT nextval('public.faculty_id_seq'::regclass) NOT NULL,
    empid character varying(25) NOT NULL,
    username_id character varying(50) NOT NULL,
    firstname character varying(100) NOT NULL,
    lastname character varying(100) NOT NULL,
    department character varying(55) NOT NULL,
    employment_status character varying(10) NOT NULL,
    email character varying(20) NOT NULL,
    mobile character varying(20) NOT NULL,
    issued_date date NOT NULL
);


ALTER TABLE public.faculty OWNER TO postgres;

--
-- Name: fine_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fine_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fine_id_seq OWNER TO postgres;

--
-- Name: fine; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fine (
    id bigint DEFAULT nextval('public.fine_id_seq'::regclass) NOT NULL,
    code character varying(20) NOT NULL,
    amount real NOT NULL
);


ALTER TABLE public.fine OWNER TO postgres;

--
-- Name: inventory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.inventory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.inventory_id_seq OWNER TO postgres;

--
-- Name: inventory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.inventory (
    id bigint DEFAULT nextval('public.inventory_id_seq'::regclass) NOT NULL,
    bookcode_id character varying(20) NOT NULL,
    total_count integer NOT NULL,
    lost_count integer NOT NULL,
    inventory_date date NOT NULL,
    received_by character varying(100) NOT NULL
);


ALTER TABLE public.inventory OWNER TO postgres;

--
-- Name: login_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.login_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.login_id_seq OWNER TO postgres;

--
-- Name: login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login (
    id bigint DEFAULT nextval('public.login_id_seq'::regclass) NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(250) NOT NULL,
    role integer NOT NULL
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: migratehistory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.migratehistory (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    migrated timestamp without time zone NOT NULL
);


ALTER TABLE public.migratehistory OWNER TO postgres;

--
-- Name: migratehistory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.migratehistory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.migratehistory_id_seq OWNER TO postgres;

--
-- Name: migratehistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.migratehistory_id_seq OWNED BY public.migratehistory.id;


--
-- Name: publisher_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.publisher_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publisher_id_seq OWNER TO postgres;

--
-- Name: publisher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.publisher (
    id bigint DEFAULT nextval('public.publisher_id_seq'::regclass) NOT NULL,
    code character varying(20) NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public.publisher OWNER TO postgres;

--
-- Name: student_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_id_seq OWNER TO postgres;

--
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student (
    id bigint DEFAULT nextval('public.student_id_seq'::regclass) NOT NULL,
    studid character varying(25) NOT NULL,
    username_id character varying(50) NOT NULL,
    firstname character varying(100) NOT NULL,
    lastname character varying(100) NOT NULL,
    course character varying(55) NOT NULL,
    classification character varying(55) NOT NULL,
    status boolean NOT NULL,
    email character varying(20) NOT NULL,
    mobile character varying(20) NOT NULL,
    enrolled_date date NOT NULL
);


ALTER TABLE public.student OWNER TO postgres;

--
-- Name: visitor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.visitor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.visitor_id_seq OWNER TO postgres;

--
-- Name: visitor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.visitor (
    id bigint DEFAULT nextval('public.visitor_id_seq'::regclass) NOT NULL,
    issuedid character varying(25) NOT NULL,
    username_id character varying(50) NOT NULL,
    firstname character varying(100) NOT NULL,
    lastname character varying(100) NOT NULL,
    profession character varying(55) NOT NULL,
    company character varying(100) NOT NULL,
    email character varying(20) NOT NULL,
    mobile character varying(20) NOT NULL,
    issued_date date NOT NULL
);


ALTER TABLE public.visitor OWNER TO postgres;

--
-- Name: migratehistory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.migratehistory ALTER COLUMN id SET DEFAULT nextval('public.migratehistory_id_seq'::regclass);


--
-- Data for Name: administrator; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.administrator (id, empid, username_id, firstname, lastname, "position", email, mobile, issued_date) FROM stdin;
\.


--
-- Data for Name: book; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.book (id, code, title, author, isbn, published_year, edition, publisher_id, category_id, description) FROM stdin;
\.


--
-- Data for Name: borrow_faculty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.borrow_faculty (id, bookcode_id, empid_id, borrowed_date, returned_date, duration, approved_by) FROM stdin;
\.


--
-- Data for Name: borrow_student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.borrow_student (id, bookcode_id, studid_id, borrowed_date, duration, returned_date, approved_by) FROM stdin;
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (id, code, name, description) FROM stdin;
\.


--
-- Data for Name: faculty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faculty (id, empid, username_id, firstname, lastname, department, employment_status, email, mobile, issued_date) FROM stdin;
\.


--
-- Data for Name: fine; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fine (id, code, amount) FROM stdin;
\.


--
-- Data for Name: inventory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.inventory (id, bookcode_id, total_count, lost_count, inventory_date, received_by) FROM stdin;
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, username, password, role) FROM stdin;
1	sjctrags	sjctrags	1
2	admin	admin	1
3	zac	zac	1
4	jimmy	jimmy	2
6	liza2	liza2	2
7	liza3	liza3	2
8	john1	john1	2
9	allan	allan	2
10	jerry	jerry	1
11	jerry2	jerry2	1
12	jerry3	jerry3	1
13	jerry4	jerry4	1
14	joal	joal	2
15	elly	elly	2
16	jem	jem	2
17	minda	minda	3
18	jerry123	jerry123	2
19	olola	olola	1
20	tuyty	rttyy	2
21	555	555	2
22	444	444	5
23	98989	89898	57
24	gfgf	gfgfg	2
\.


--
-- Data for Name: migratehistory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.migratehistory (id, name, migrated) FROM stdin;
1	0001_migration_202404112054	2024-04-11 12:54:37.886794
\.


--
-- Data for Name: publisher; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.publisher (id, code, name) FROM stdin;
\.


--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student (id, studid, username_id, firstname, lastname, course, classification, status, email, mobile, enrolled_date) FROM stdin;
\.


--
-- Data for Name: visitor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.visitor (id, issuedid, username_id, firstname, lastname, profession, company, email, mobile, issued_date) FROM stdin;
\.


--
-- Name: administrator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.administrator_id_seq', 1, false);


--
-- Name: book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.book_id_seq', 1, false);


--
-- Name: borrow_faculty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.borrow_faculty_id_seq', 1, false);


--
-- Name: borrow_student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.borrow_student_id_seq', 1, false);


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_id_seq', 1, false);


--
-- Name: faculty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.faculty_id_seq', 1, false);


--
-- Name: fine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fine_id_seq', 1, false);


--
-- Name: inventory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.inventory_id_seq', 1, false);


--
-- Name: login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_id_seq', 24, true);


--
-- Name: migratehistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.migratehistory_id_seq', 1, true);


--
-- Name: publisher_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.publisher_id_seq', 1, false);


--
-- Name: student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_id_seq', 1, false);


--
-- Name: visitor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.visitor_id_seq', 1, false);


--
-- Name: administrator administrator_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrator
    ADD CONSTRAINT administrator_pkey PRIMARY KEY (id);


--
-- Name: book book_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (id);


--
-- Name: borrow_faculty borrow_faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrow_faculty
    ADD CONSTRAINT borrow_faculty_pkey PRIMARY KEY (id);


--
-- Name: borrow_student borrow_student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrow_student
    ADD CONSTRAINT borrow_student_pkey PRIMARY KEY (id);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- Name: faculty faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (id);


--
-- Name: fine fine_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fine
    ADD CONSTRAINT fine_pkey PRIMARY KEY (id);


--
-- Name: inventory inventory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_pkey PRIMARY KEY (id);


--
-- Name: login login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_pkey PRIMARY KEY (id);


--
-- Name: migratehistory migratehistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.migratehistory
    ADD CONSTRAINT migratehistory_pkey PRIMARY KEY (id);


--
-- Name: publisher publisher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publisher
    ADD CONSTRAINT publisher_pkey PRIMARY KEY (id);


--
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);


--
-- Name: visitor visitor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visitor
    ADD CONSTRAINT visitor_pkey PRIMARY KEY (id);


--
-- Name: administrator_empid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX administrator_empid ON public.administrator USING btree (empid);


--
-- Name: administrator_username_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX administrator_username_id ON public.administrator USING btree (username_id);


--
-- Name: book_category_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX book_category_id ON public.book USING btree (category_id);


--
-- Name: book_code; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX book_code ON public.book USING btree (code);


--
-- Name: book_publisher_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX book_publisher_id ON public.book USING btree (publisher_id);


--
-- Name: borrowfaculty_bookcode_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX borrowfaculty_bookcode_id ON public.borrow_faculty USING btree (bookcode_id);


--
-- Name: borrowfaculty_empid_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX borrowfaculty_empid_id ON public.borrow_faculty USING btree (empid_id);


--
-- Name: borrowstudent_bookcode_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX borrowstudent_bookcode_id ON public.borrow_student USING btree (bookcode_id);


--
-- Name: borrowstudent_studid_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX borrowstudent_studid_id ON public.borrow_student USING btree (studid_id);


--
-- Name: category_code; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX category_code ON public.category USING btree (code);


--
-- Name: faculty_empid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX faculty_empid ON public.faculty USING btree (empid);


--
-- Name: faculty_username_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX faculty_username_id ON public.faculty USING btree (username_id);


--
-- Name: fine_code; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX fine_code ON public.fine USING btree (code);


--
-- Name: inventory_bookcode_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX inventory_bookcode_id ON public.inventory USING btree (bookcode_id);


--
-- Name: login_username; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX login_username ON public.login USING btree (username);


--
-- Name: publisher_code; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX publisher_code ON public.publisher USING btree (code);


--
-- Name: student_studid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX student_studid ON public.student USING btree (studid);


--
-- Name: student_username_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_username_id ON public.student USING btree (username_id);


--
-- Name: visitor_issuedid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX visitor_issuedid ON public.visitor USING btree (issuedid);


--
-- Name: visitor_username_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX visitor_username_id ON public.visitor USING btree (username_id);


--
-- Name: administrator administrator_username_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrator
    ADD CONSTRAINT administrator_username_id_fkey FOREIGN KEY (username_id) REFERENCES public.login(username);


--
-- Name: book book_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category(code);


--
-- Name: book book_publisher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_publisher_id_fkey FOREIGN KEY (publisher_id) REFERENCES public.publisher(code);


--
-- Name: borrow_faculty borrow_faculty_bookcode_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrow_faculty
    ADD CONSTRAINT borrow_faculty_bookcode_id_fkey FOREIGN KEY (bookcode_id) REFERENCES public.book(code);


--
-- Name: borrow_faculty borrow_faculty_empid_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrow_faculty
    ADD CONSTRAINT borrow_faculty_empid_id_fkey FOREIGN KEY (empid_id) REFERENCES public.faculty(empid);


--
-- Name: borrow_student borrow_student_bookcode_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrow_student
    ADD CONSTRAINT borrow_student_bookcode_id_fkey FOREIGN KEY (bookcode_id) REFERENCES public.book(code);


--
-- Name: borrow_student borrow_student_studid_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.borrow_student
    ADD CONSTRAINT borrow_student_studid_id_fkey FOREIGN KEY (studid_id) REFERENCES public.student(studid);


--
-- Name: faculty faculty_username_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_username_id_fkey FOREIGN KEY (username_id) REFERENCES public.login(username);


--
-- Name: inventory inventory_bookcode_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_bookcode_id_fkey FOREIGN KEY (bookcode_id) REFERENCES public.book(code);


--
-- Name: student student_username_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_username_id_fkey FOREIGN KEY (username_id) REFERENCES public.login(username);


--
-- Name: visitor visitor_username_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.visitor
    ADD CONSTRAINT visitor_username_id_fkey FOREIGN KEY (username_id) REFERENCES public.login(username);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


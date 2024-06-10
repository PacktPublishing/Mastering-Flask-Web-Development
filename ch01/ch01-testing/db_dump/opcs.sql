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
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    age integer,
    "position" character varying(60),
    emp_started date,
    emp_status character(8) DEFAULT 'inactive'::bpchar NOT NULL
);


ALTER TABLE public.admin OWNER TO postgres;

--
-- Name: all_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.all_user (
    id integer NOT NULL,
    username character varying(45) NOT NULL,
    password character varying(45) NOT NULL,
    user_approved date NOT NULL
);


ALTER TABLE public.all_user OWNER TO postgres;

--
-- Name: counselor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.counselor (
    id integer NOT NULL,
    cid character varying(45) NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    age integer,
    "position" character varying(60),
    profession_started date
);


ALTER TABLE public.counselor OWNER TO postgres;

--
-- Name: patient; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patient (
    id integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    age integer,
    gender character(1),
    civil_status character varying(20),
    address character varying(100),
    mobile character varying(25),
    occupation character varying(60),
    nationality character varying(45),
    cid character varying(45),
    counseling_started date,
    counseling_ended date
);


ALTER TABLE public.patient OWNER TO postgres;

--
-- Name: patient_contract; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patient_contract (
    id integer NOT NULL,
    pid integer NOT NULL,
    approved_by character varying(100) NOT NULL,
    approved_date date NOT NULL,
    health_care_provider character varying(100) NOT NULL,
    payment_mode character varying(20) NOT NULL,
    amount_paid double precision NOT NULL,
    amount_due double precision NOT NULL
);


ALTER TABLE public.patient_contract OWNER TO postgres;

--
-- Name: patient_contract_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.patient_contract_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patient_contract_id_seq OWNER TO postgres;

--
-- Name: patient_contract_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.patient_contract_id_seq OWNED BY public.patient_contract.id;


--
-- Name: patient_score_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.patient_score_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patient_score_id_seq OWNER TO postgres;

--
-- Name: patient_score; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patient_score (
    id integer DEFAULT nextval('public.patient_score_id_seq'::regclass) NOT NULL,
    pid integer,
    qid integer,
    score real,
    total real,
    status character varying(45),
    percentage numeric(5,2) DEFAULT 0.0 NOT NULL
);


ALTER TABLE public.patient_score OWNER TO postgres;

--
-- Name: question_choices_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.question_choices_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_choices_id_seq OWNER TO postgres;

--
-- Name: question_choices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.question_choices (
    id integer DEFAULT nextval('public.question_choices_id_seq'::regclass) NOT NULL,
    choice character(1) NOT NULL,
    choice_text text NOT NULL,
    correct_choice boolean NOT NULL,
    item_id integer,
    qid integer
);


ALTER TABLE public.question_choices OWNER TO postgres;

--
-- Name: question_details; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.question_details (
    id integer NOT NULL,
    cid character varying(45) NOT NULL,
    pid integer NOT NULL,
    exam_date date NOT NULL,
    duration integer NOT NULL
);


ALTER TABLE public.question_details OWNER TO postgres;

--
-- Name: question_pool_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.question_pool_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_pool_id_seq OWNER TO postgres;

--
-- Name: question_pool; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.question_pool (
    id integer DEFAULT nextval('public.question_pool_id_seq'::regclass) NOT NULL,
    question text NOT NULL,
    type integer NOT NULL,
    qid integer
);


ALTER TABLE public.question_pool OWNER TO postgres;

--
-- Name: question_subjective_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.question_subjective_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_subjective_id_seq OWNER TO postgres;

--
-- Name: question_subjective; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.question_subjective (
    id integer DEFAULT nextval('public.question_subjective_id_seq'::regclass) NOT NULL,
    correct_answer text NOT NULL,
    item_id integer,
    qid integer
);


ALTER TABLE public.question_subjective OWNER TO postgres;

--
-- Name: signup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.signup (
    id integer NOT NULL,
    username character varying(45) NOT NULL,
    password character varying(45) NOT NULL,
    user_type integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    cid character varying(45) DEFAULT 'NA'::character varying
);


ALTER TABLE public.signup OWNER TO postgres;

--
-- Name: signup_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.signup_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.signup_id_seq OWNER TO postgres;

--
-- Name: signup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.signup_id_seq OWNED BY public.signup.id;


--
-- Name: patient_contract id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_contract ALTER COLUMN id SET DEFAULT nextval('public.patient_contract_id_seq'::regclass);


--
-- Name: signup id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.signup ALTER COLUMN id SET DEFAULT nextval('public.signup_id_seq'::regclass);


--
-- Data for Name: admin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.admin (id, firstname, lastname, age, "position", emp_started, emp_status) FROM stdin;
222	Sherwin	Tragura	43	Supervisor	2023-02-03	active  
676	Anna	Anna	18	Supervisor	2023-02-16	active  
787	Joanna	Lim	54	Tech Manager	2023-03-08	active  
555	Kilo	Kilo	45	Security Engr	2023-03-22	active  
890	gene	gene	33	Supervisor	2023-03-30	active  
45454	pose	pose	33	Supervisor	2023-03-22	active  
\.


--
-- Data for Name: all_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.all_user (id, username, password, user_approved) FROM stdin;
222	sjctrags	sjctrags	2023-02-26
567	wewewe	aaasa	2023-02-26
1111	kulas	kulas	2023-02-26
676	anna	anna	2023-02-26
908	jean	jean	2023-02-26
435	holly	holly	2023-02-26
787	admin	admin	2023-03-04
386	kris	kris	2023-03-04
555	kulay	kulay	2023-03-05
3879	jeje	jeje	2023-03-05
1211	kerry	kerry	2023-03-05
890	gene	gene	2023-03-06
45454	pose	pose	2023-03-06
\.


--
-- Data for Name: counselor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.counselor (id, cid, firstname, lastname, age, "position", profession_started) FROM stdin;
567	ABCD1234	Joey	Zach	43	Supervisor	2023-02-02
908	HJGFDC	Jean	Jean	44	Supervisor	2023-02-16
386	KLBNMV	asas	asasa	34	Supervisor	2023-03-16
3879	HJNB6778	Jerry	Jerome	33	Supervisor	2023-03-15
\.


--
-- Data for Name: patient; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patient (id, firstname, lastname, age, gender, civil_status, address, mobile, occupation, nationality, cid, counseling_started, counseling_ended) FROM stdin;
1111	Nicholas	Julie	43	f	single	Unit 1003 South Tower, Sheridan Towers, Sheridan St.	+639257175107	asas	asasa	ABCD1234	2023-02-10	2023-02-24
435	Holly	Holly	33	f	married	Unit 2B 500 Hizon St	+639399175107	asas	asasa	HJGFDC	2023-02-09	2023-02-27
1211	kerry	kerry	54	f	single	Makati	09334567890	Actress	USA	HJNB6778	2023-03-08	2023-03-23
\.


--
-- Data for Name: patient_contract; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patient_contract (id, pid, approved_by, approved_date, health_care_provider, payment_mode, amount_paid, amount_due) FROM stdin;
4	1111	Joanna Lumley	2023-09-19	Intellicare	check	0	5000
5	435	Zelu Kerr	2023-09-28	Medicard	cash	3000	2000
6	1211	Gelli Keber	2023-10-19	None	cash	5000	0
\.


--
-- Data for Name: patient_score; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patient_score (id, pid, qid, score, total, status, percentage) FROM stdin;
4	1111	567	55.5	100	conditional	55.50
5	1111	567	55.5	100	conditional	55.50
6	435	568	67.8	120	conditional	56.50
7	435	568	67.8	120	conditional	56.50
8	435	568	32	44	passed	72.73
13	1111	568	87	100	passed	87.00
14	1111	568	87	100	passed	87.00
15	1111	568	87	100	passed	87.00
16	1111	568	87	100	passed	87.00
17	1111	568	87	100	passed	87.00
18	1111	568	87	100	passed	87.00
19	1111	568	87	100	passed	87.00
20	1111	568	87	100	passed	87.00
21	1111	568	87	100	passed	87.00
22	1111	568	87	100	passed	87.00
23	1111	568	87	100	passed	87.00
24	1111	568	87	100	passed	87.00
25	1111	568	87	100	passed	87.00
26	1111	568	87	100	passed	87.00
27	1111	568	87	100	passed	87.00
28	1111	568	87	100	passed	87.00
29	1111	568	87	100	passed	87.00
30	1111	568	87	100	passed	87.00
31	1111	568	87	100	passed	87.00
32	1111	568	87	100	passed	87.00
33	1111	568	87	100	passed	87.00
34	1111	568	87	100	passed	87.00
35	1111	568	87	100	passed	87.00
36	1111	568	87	100	passed	87.00
37	1111	568	87	100	passed	87.00
38	1111	568	87	100	passed	87.00
39	1111	568	87	100	passed	87.00
40	1111	568	87	100	passed	87.00
41	1111	568	87	100	passed	87.00
42	1111	568	87	100	passed	87.00
43	1111	568	87	100	passed	87.00
44	1111	568	87	100	passed	87.00
45	1111	568	87	100	passed	87.00
46	1111	568	87	100	passed	87.00
47	1111	568	87	100	passed	87.00
48	1111	568	87	100	passed	87.00
49	1111	568	87	100	passed	87.00
50	1111	568	87	100	passed	87.00
51	1111	568	87	100	passed	87.00
52	1111	568	87	100	passed	87.00
53	1111	568	87	100	passed	87.00
54	1111	568	87	100	passed	87.00
55	1111	568	87	100	passed	87.00
56	1111	568	87	100	passed	87.00
57	1111	568	87	100	passed	87.00
58	1111	568	87	100	passed	87.00
59	1111	568	87	100	passed	87.00
60	1111	568	87	100	passed	87.00
61	1111	568	87	100	passed	87.00
62	1111	568	87	100	passed	87.00
63	1111	568	87	100	passed	87.00
64	1111	568	87	100	passed	87.00
65	1111	568	87	100	passed	87.00
66	1111	568	87	100	passed	87.00
67	1111	568	87	100	passed	87.00
68	1111	568	87	100	passed	87.00
69	1111	568	87	100	passed	87.00
70	1111	568	87	100	passed	87.00
71	1111	568	87	100	passed	87.00
72	1111	568	87	100	passed	87.00
73	1111	568	87	100	passed	87.00
74	1111	568	87	100	passed	87.00
75	1111	568	87	100	passed	87.00
76	1111	568	87	100	passed	87.00
77	1111	568	87	100	passed	87.00
78	1111	568	87	100	passed	87.00
\.


--
-- Data for Name: question_choices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.question_choices (id, choice, choice_text, correct_choice, item_id, qid) FROM stdin;
45	a	chicken	f	24	567
46	b	pork	f	24	567
47	c	rice	f	24	567
48	d	beef	t	24	567
49	a	chicken	f	25	567
50	b	pork	f	25	567
51	c	rice	f	25	567
52	d	beef	t	25	567
53	a	dfdfd	f	26	568
54	b	dfdfdf	f	26	568
55	c	dfdfd	t	26	568
56	d	fdfdfd	f	26	568
57	a	dfdf	f	31	789
58	b	dfd	f	31	789
59	c	fdfd	f	31	789
60	d	fdfd	t	31	789
\.


--
-- Data for Name: question_details; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.question_details (id, cid, pid, exam_date, duration) FROM stdin;
567	ABCD1234	435	2023-02-15	2
568	HJGFDC	435	2023-03-01	3
789	KLBNMV	1111	2023-03-16	4
6654	HJNB6778	1111	2023-03-24	2
\.


--
-- Data for Name: question_pool; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.question_pool (id, question, type, qid) FROM stdin;
21	Yuck yukc	2	567
22	Yuck yukc	2	567
23	Why do development?	2	567
24	What is your favorite food?	1	567
25	What is your favorite food?	1	567
26	dfdfdfd	1	568
27	dfdfd	2	568
28	dfdfd	2	568
29	dfdfd	2	568
30	dfdfd	2	568
31	dfdf	1	789
\.


--
-- Data for Name: question_subjective; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.question_subjective (id, correct_answer, item_id, qid) FROM stdin;
2	dssdsds	21	567
3	dssdsds	22	567
4	To help others	23	567
5	dfdfdfd	27	568
6	dfdfdfd	28	568
7	dfdfdfd	29	568
8	dfdfdfd	30	568
\.


--
-- Data for Name: signup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.signup (id, username, password, user_type, firstname, lastname, cid) FROM stdin;
3	sjctrags	sjctrags	1	Sherwin	Tragura	
4	admin	admin	1	Joanna	Lim	
6	kulas	kulas	3	Nicholas	Julie	
5	wewewe	aaasa	2	Joey	Zach	ABCD1234
7	anna	anna	1	Anna	Anna	
8	jean	jean	2	Jean	Jean	HJGFDC
9	holly	holly	3	Holly	Holly	
10	kris	kris	2	asas	asasa	KLBNMV
11	kulay	kulay	1	Kilo	Kilo	
12	jeje	jeje	2	Jerry	Jerome	HJNB6778
13	kerry	kerry	3	kerry	kerry	
14	jonny	jonny	2	helo	helo	FGHY3232
16	bbb	bbb	3	bbb	bbb	FGHY3232
17	gene	gene	1	gene	gene	FGHY3232
18	kreg	kreg	2	kreg	kreg	HJNB6778
19	jelo	jelo	3	jelo	jelo	
20	hulo	hulo	1	hulo	hulo	
21	pose	pose	1	pose	pose	
22	sdsds	sdsds	1	sdsd	sdsds	
24	owen	owen	2	Owen Salvador	Estabillo	CGFCDS
\.


--
-- Name: patient_contract_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.patient_contract_id_seq', 6, true);


--
-- Name: patient_score_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.patient_score_id_seq', 78, true);


--
-- Name: question_choices_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.question_choices_id_seq', 60, true);


--
-- Name: question_pool_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.question_pool_id_seq', 31, true);


--
-- Name: question_subjective_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.question_subjective_id_seq', 8, true);


--
-- Name: signup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.signup_id_seq', 81, true);


--
-- Name: admin admin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id);


--
-- Name: all_user all_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.all_user
    ADD CONSTRAINT all_user_pkey PRIMARY KEY (id);


--
-- Name: all_user all_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.all_user
    ADD CONSTRAINT all_user_username_key UNIQUE (username);


--
-- Name: counselor counselor_cid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counselor
    ADD CONSTRAINT counselor_cid_key UNIQUE (cid);


--
-- Name: counselor counselor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counselor
    ADD CONSTRAINT counselor_pkey PRIMARY KEY (id);


--
-- Name: patient_contract patient_contract_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_contract
    ADD CONSTRAINT patient_contract_pkey PRIMARY KEY (id);


--
-- Name: patient patient_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient
    ADD CONSTRAINT patient_pkey PRIMARY KEY (id);


--
-- Name: patient_score patient_score_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_score
    ADD CONSTRAINT patient_score_pkey PRIMARY KEY (id);


--
-- Name: question_choices question_choices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_choices
    ADD CONSTRAINT question_choices_pkey PRIMARY KEY (id);


--
-- Name: question_details question_details_cid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_details
    ADD CONSTRAINT question_details_cid_key UNIQUE (cid);


--
-- Name: question_details question_details_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_details
    ADD CONSTRAINT question_details_pkey PRIMARY KEY (id);


--
-- Name: question_pool question_pool_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_pool
    ADD CONSTRAINT question_pool_id_pkey PRIMARY KEY (id);


--
-- Name: question_subjective question_subjective_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_subjective
    ADD CONSTRAINT question_subjective_id_pkey PRIMARY KEY (id);


--
-- Name: signup signup_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.signup
    ADD CONSTRAINT signup_pkey PRIMARY KEY (id);


--
-- Name: signup signup_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.signup
    ADD CONSTRAINT signup_username_key UNIQUE (username);


--
-- Name: admin fk_admin_user1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT fk_admin_user1 FOREIGN KEY (id) REFERENCES public.all_user(id);


--
-- Name: counselor fk_counselor_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.counselor
    ADD CONSTRAINT fk_counselor_user FOREIGN KEY (id) REFERENCES public.all_user(id);


--
-- Name: patient fk_patient_counselor1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient
    ADD CONSTRAINT fk_patient_counselor1 FOREIGN KEY (cid) REFERENCES public.counselor(cid);


--
-- Name: patient_score fk_patient_score_patient1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_score
    ADD CONSTRAINT fk_patient_score_patient1 FOREIGN KEY (pid) REFERENCES public.patient(id);


--
-- Name: patient_score fk_patient_score_question_details1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_score
    ADD CONSTRAINT fk_patient_score_question_details1 FOREIGN KEY (qid) REFERENCES public.question_details(id);


--
-- Name: patient fk_patient_user1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient
    ADD CONSTRAINT fk_patient_user1 FOREIGN KEY (id) REFERENCES public.all_user(id);


--
-- Name: question_details fk_question_details_counselor1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_details
    ADD CONSTRAINT fk_question_details_counselor1 FOREIGN KEY (cid) REFERENCES public.counselor(cid);


--
-- Name: question_details fk_question_details_patient1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_details
    ADD CONSTRAINT fk_question_details_patient1 FOREIGN KEY (pid) REFERENCES public.patient(id);


--
-- Name: patient_contract patient_contract_pid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_contract
    ADD CONSTRAINT patient_contract_pid_fkey FOREIGN KEY (pid) REFERENCES public.patient(id);


--
-- Name: question_choices question_choices_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_choices
    ADD CONSTRAINT question_choices_item_id_fkey FOREIGN KEY (item_id) REFERENCES public.question_pool(id);


--
-- Name: question_choices question_choices_qid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_choices
    ADD CONSTRAINT question_choices_qid_fkey FOREIGN KEY (qid) REFERENCES public.question_details(id);


--
-- Name: question_pool question_pool_qid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_pool
    ADD CONSTRAINT question_pool_qid_fkey FOREIGN KEY (qid) REFERENCES public.question_details(id);


--
-- Name: question_subjective question_subjective_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_subjective
    ADD CONSTRAINT question_subjective_item_id_fkey FOREIGN KEY (item_id) REFERENCES public.question_pool(id);


--
-- Name: question_subjective question_subjective_qid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question_subjective
    ADD CONSTRAINT question_subjective_qid_fkey FOREIGN KEY (qid) REFERENCES public.question_details(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


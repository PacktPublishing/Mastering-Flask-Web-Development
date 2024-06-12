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
    middlename character varying(45) NOT NULL,
    email character varying(45) NOT NULL,
    mobile character varying(45) NOT NULL
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
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    id integer NOT NULL,
    firstname character varying(55),
    middlename character varying(55),
    lastname character varying(55),
    mobile character(12),
    address character varying(100),
    email character varying(20),
    status character varying(45)
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- Name: delivery_officer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.delivery_officer (
    id integer NOT NULL,
    firstname character varying(55) NOT NULL,
    lastname character varying(55) NOT NULL,
    middlename character varying(55) NOT NULL,
    mobile character(15) NOT NULL,
    address character varying(100) NOT NULL,
    email character varying(20) NOT NULL,
    status character varying(45) NOT NULL
);


ALTER TABLE public.delivery_officer OWNER TO postgres;

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
    id integer DEFAULT nextval('public.login_id_seq'::regclass) NOT NULL,
    username character varying(45) NOT NULL,
    password character varying(45) NOT NULL,
    user_type integer NOT NULL
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_id_seq OWNER TO postgres;

--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    id integer DEFAULT nextval('public.orders_id_seq'::regclass) NOT NULL,
    pid integer NOT NULL,
    order_no character varying(20) NOT NULL,
    cid integer NOT NULL,
    order_date date NOT NULL
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: payment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.payment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.payment_id_seq OWNER TO postgres;

--
-- Name: payment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payment (
    id integer DEFAULT nextval('public.payment_id_seq'::regclass) NOT NULL,
    order_no character varying(20) NOT NULL,
    amount double precision NOT NULL,
    mode_payment integer NOT NULL,
    ref_no character varying(20) NOT NULL,
    date_payment date NOT NULL
);


ALTER TABLE public.payment OWNER TO postgres;

--
-- Name: payment_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.payment_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.payment_type_id_seq OWNER TO postgres;

--
-- Name: payment_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payment_type (
    id integer DEFAULT nextval('public.payment_type_id_seq'::regclass) NOT NULL,
    name character varying(45) NOT NULL
);


ALTER TABLE public.payment_type OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO postgres;

--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id integer DEFAULT nextval('public.products_id_seq'::regclass) NOT NULL,
    name character varying(100) NOT NULL,
    price double precision NOT NULL,
    code character varying(45) NOT NULL
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: shipping_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shipping_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shipping_id_seq OWNER TO postgres;

--
-- Name: shipping; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shipping (
    id integer DEFAULT nextval('public.shipping_id_seq'::regclass) NOT NULL,
    cid integer NOT NULL,
    pay_id integer NOT NULL,
    did integer NOT NULL,
    amount double precision NOT NULL,
    status character varying(45) NOT NULL,
    date_shipping date NOT NULL
);


ALTER TABLE public.shipping OWNER TO postgres;

--
-- Name: shipping_details_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shipping_details_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shipping_details_id_seq OWNER TO postgres;

--
-- Name: shipping_details; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shipping_details (
    id integer DEFAULT nextval('public.shipping_details_id_seq'::regclass) NOT NULL,
    sid integer NOT NULL,
    qty integer NOT NULL,
    amount double precision NOT NULL
);


ALTER TABLE public.shipping_details OWNER TO postgres;

--
-- Data for Name: admin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.admin (id, firstname, lastname, middlename, email, mobile) FROM stdin;
1	Sherwin John	Tragura	Calleja	sjctrags@gmail.com	039399175107
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer (id, firstname, middlename, lastname, mobile, address, email, status) FROM stdin;
2	Sherwin John	Calleja	Tragura	09399175107 	Unit 1003 South Tower, Sheridan Towers, Sheridan St.	sjctrags@gmail.com	active
21	Gelo	Santos	De Asis	09399175107 	Pasig City	gelo@gmail.com	active
3	ffgfg	fgfgf	fgfg	fgfgfgf     	fgfgf	anna@gmail.com	inactive
\.


--
-- Data for Name: delivery_officer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.delivery_officer (id, firstname, lastname, middlename, mobile, address, email, status) FROM stdin;
456	Sherwin John	Tragura	Calleja	09399175107    	Unit 1003 South Tower, Sheridan Towers, Sheridan St.	sjctrags@gmail.com	active
54545	Joanna	Lumley	Cruz	0992932323     	UK	joanna@gmail.com	active
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, username, password, user_type) FROM stdin;
1	sjctrags	admin2255	1
2	admin	admin	2
3	anna	anna2255	2
11	kira	kira	2
12	joanna	joanna	1
20	owen	owen	1
21	gelo	gelo	2
23	kris	kris	1
28	julie	julie	1
31	kelly	kelly	2
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (id, pid, order_no, cid, order_date) FROM stdin;
1	1	ABC-1234	2	2023-03-17
6	1	EDFG	21	2023-04-28
\.


--
-- Data for Name: payment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payment (id, order_no, amount, mode_payment, ref_no, date_payment) FROM stdin;
1	ABC-1234	12000	2	PAY-12345	2023-03-17
\.


--
-- Data for Name: payment_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payment_type (id, name) FROM stdin;
1	credit card
2	debit card
3	wallet
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (id, name, price, code) FROM stdin;
1	Pen	75	SCH-PEN-111
2	paper	500.4	SCH-PAPER-333
3	paper	45.9	SCH-PAPER-01
13	eraser	125	SCH-8977
\.


--
-- Data for Name: shipping; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shipping (id, cid, pay_id, did, amount, status, date_shipping) FROM stdin;
1	21	1	54545	3198	active	2023-04-29
2	21	1	456	12000	inactive	2023-04-19
\.


--
-- Data for Name: shipping_details; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shipping_details (id, sid, qty, amount) FROM stdin;
\.


--
-- Name: login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_id_seq', 32, true);


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_seq', 6, true);


--
-- Name: payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.payment_id_seq', 1, true);


--
-- Name: payment_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.payment_type_id_seq', 3, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 13, true);


--
-- Name: shipping_details_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shipping_details_id_seq', 1, false);


--
-- Name: shipping_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shipping_id_seq', 2, true);


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
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);


--
-- Name: delivery_officer delivery_officer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.delivery_officer
    ADD CONSTRAINT delivery_officer_pkey PRIMARY KEY (id);


--
-- Name: login login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_pkey PRIMARY KEY (id);


--
-- Name: login login_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_username_key UNIQUE (username);


--
-- Name: orders orders_order_no_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_order_no_key UNIQUE (order_no);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- Name: payment payment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (id);


--
-- Name: payment payment_ref_no_ukey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_ref_no_ukey UNIQUE (ref_no);


--
-- Name: payment_type payment_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment_type
    ADD CONSTRAINT payment_type_pkey PRIMARY KEY (id);


--
-- Name: products products_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_code_key UNIQUE (code);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: shipping_details shipping_details_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipping_details
    ADD CONSTRAINT shipping_details_pkey PRIMARY KEY (id);


--
-- Name: shipping_details shipping_details_sid_ukey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipping_details
    ADD CONSTRAINT shipping_details_sid_ukey UNIQUE (sid);


--
-- Name: shipping shipping_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipping
    ADD CONSTRAINT shipping_pkey PRIMARY KEY (id);


--
-- Name: admin fk_admin_login1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT fk_admin_login1 FOREIGN KEY (id) REFERENCES public.login(id);


--
-- Name: customer fk_customer_login; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT fk_customer_login FOREIGN KEY (id) REFERENCES public.login(id);


--
-- Name: orders fk_order_customer1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT fk_order_customer1 FOREIGN KEY (cid) REFERENCES public.customer(id);


--
-- Name: orders fk_order_products1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT fk_order_products1 FOREIGN KEY (pid) REFERENCES public.products(id);


--
-- Name: payment fk_payment_order1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT fk_payment_order1 FOREIGN KEY (order_no) REFERENCES public.orders(order_no);


--
-- Name: payment fk_payment_payment_type1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT fk_payment_payment_type1 FOREIGN KEY (mode_payment) REFERENCES public.payment_type(id);


--
-- Name: shipping fk_shipping_customer1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipping
    ADD CONSTRAINT fk_shipping_customer1 FOREIGN KEY (cid) REFERENCES public.customer(id);


--
-- Name: shipping fk_shipping_delivery_officer1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipping
    ADD CONSTRAINT fk_shipping_delivery_officer1 FOREIGN KEY (did) REFERENCES public.delivery_officer(id);


--
-- Name: shipping_details fk_shipping_details_shipping1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipping_details
    ADD CONSTRAINT fk_shipping_details_shipping1 FOREIGN KEY (sid) REFERENCES public.shipping(id);


--
-- Name: shipping fk_shipping_payment1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shipping
    ADD CONSTRAINT fk_shipping_payment1 FOREIGN KEY (pay_id) REFERENCES public.payment(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


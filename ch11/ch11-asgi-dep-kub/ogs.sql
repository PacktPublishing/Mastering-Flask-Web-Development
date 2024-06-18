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
    enrolled_date date NOT NULL
);


ALTER TABLE public.administrator OWNER TO postgres;

--
-- Name: brand_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.brand_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.brand_id_seq OWNER TO postgres;

--
-- Name: brand; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.brand (
    id bigint DEFAULT nextval('public.brand_id_seq'::regclass) NOT NULL,
    code character varying(20) NOT NULL,
    name character varying(100) NOT NULL,
    description character varying(200) NOT NULL
);


ALTER TABLE public.brand OWNER TO postgres;

--
-- Name: cart_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cart_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cart_id_seq OWNER TO postgres;

--
-- Name: cart; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cart (
    id bigint DEFAULT nextval('public.cart_id_seq'::regclass) NOT NULL,
    orderid character varying(50) NOT NULL,
    ordered_date date NOT NULL,
    ordered_by_id character varying(50) NOT NULL,
    total real
);


ALTER TABLE public.cart OWNER TO postgres;

--
-- Name: cart_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cart_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cart_item_id_seq OWNER TO postgres;

--
-- Name: cart_item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cart_item (
    id bigint DEFAULT nextval('public.cart_item_id_seq'::regclass) NOT NULL,
    orderid_id character varying(50) NOT NULL,
    pcode_id character varying(20) NOT NULL,
    qty integer NOT NULL
);


ALTER TABLE public.cart_item OWNER TO postgres;

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
-- Name: customer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.customer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.customer_id_seq OWNER TO postgres;

--
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    id bigint DEFAULT nextval('public.customer_id_seq'::regclass) NOT NULL,
    custid character varying(25) NOT NULL,
    type character varying(25) NOT NULL,
    username_id character varying(50) NOT NULL,
    firstname character varying(100) NOT NULL,
    lastname character varying(100) NOT NULL,
    "position" character varying(100) NOT NULL,
    email character varying(20) NOT NULL,
    mobile character varying(20) NOT NULL,
    enrolled_date date NOT NULL
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- Name: discount_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.discount_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.discount_id_seq OWNER TO postgres;

--
-- Name: discount; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.discount (
    id bigint DEFAULT nextval('public.discount_id_seq'::regclass) NOT NULL,
    code character varying(20) NOT NULL,
    rate real NOT NULL
);


ALTER TABLE public.discount OWNER TO postgres;

--
-- Name: invoice_request_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.invoice_request_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.invoice_request_id_seq OWNER TO postgres;

--
-- Name: invoice_request; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.invoice_request (
    id bigint DEFAULT nextval('public.invoice_request_id_seq'::regclass) NOT NULL,
    code character varying(50) NOT NULL,
    pcode_id character varying(20) NOT NULL,
    purchase_date date NOT NULL
);


ALTER TABLE public.invoice_request OWNER TO postgres;

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
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO postgres;

--
-- Name: product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product (
    id bigint DEFAULT nextval('public.product_id_seq'::regclass) NOT NULL,
    code character varying(20) NOT NULL,
    name character varying(100) NOT NULL,
    btype_id character varying(20) NOT NULL,
    ctype_id character varying(20) NOT NULL,
    unit_type character varying(100) NOT NULL,
    sell_price real NOT NULL,
    purchase_price real NOT NULL,
    discount_id character varying(20) NOT NULL
);


ALTER TABLE public.product OWNER TO postgres;

--
-- Name: purchase_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.purchase_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.purchase_id_seq OWNER TO postgres;

--
-- Name: purchase; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.purchase (
    id bigint DEFAULT nextval('public.purchase_id_seq'::regclass) NOT NULL,
    orderid_id character varying(50) NOT NULL,
    payment_date date NOT NULL,
    received_by character varying(100) NOT NULL
);


ALTER TABLE public.purchase OWNER TO postgres;

--
-- Name: stock_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stock_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stock_id_seq OWNER TO postgres;

--
-- Name: stock; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stock (
    id bigint DEFAULT nextval('public.stock_id_seq'::regclass) NOT NULL,
    sid_id character varying(20) NOT NULL,
    invcode_id character varying(50) NOT NULL,
    qty integer NOT NULL,
    payment_date date,
    received_date date NOT NULL,
    recieved_by character varying(100) NOT NULL
);


ALTER TABLE public.stock OWNER TO postgres;

--
-- Name: supplier_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.supplier_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.supplier_id_seq OWNER TO postgres;

--
-- Name: supplier; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.supplier (
    id bigint DEFAULT nextval('public.supplier_id_seq'::regclass) NOT NULL,
    sid character varying(20) NOT NULL,
    company character varying(100) NOT NULL,
    email character varying(20) NOT NULL,
    bank_name character varying(50) NOT NULL,
    bank_account character varying(50) NOT NULL,
    mobile character varying(20) NOT NULL,
    approved_date date NOT NULL
);


ALTER TABLE public.supplier OWNER TO postgres;

--
-- Name: migratehistory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.migratehistory ALTER COLUMN id SET DEFAULT nextval('public.migratehistory_id_seq'::regclass);


--
-- Data for Name: administrator; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.administrator (id, empid, username_id, firstname, lastname, "position", email, mobile, enrolled_date) FROM stdin;
2	OGS-100	sjctrags	Sherwin John	Tragura	System Administrator	sjctrags@yahoo.com	+39393915106	2010-10-10
\.


--
-- Data for Name: brand; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.brand (id, code, name, description) FROM stdin;
1	BCH	Bench Clothing Ltd.	This is a garment company.
\.


--
-- Data for Name: cart; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cart (id, orderid, ordered_date, ordered_by_id, total) FROM stdin;
\.


--
-- Data for Name: cart_item; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cart_item (id, orderid_id, pcode_id, qty) FROM stdin;
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (id, code, name, description) FROM stdin;
\.


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer (id, custid, type, username_id, firstname, lastname, "position", email, mobile, enrolled_date) FROM stdin;
1	CUST-100	Gold	owen	Owen Salvador	Estabillo	Customer 1	owenestab@yahoo.com	+6323434343	2020-05-10
2	CUST-101	Silver	joanna	Joanna	Lumley	Customer 2	joanna@yahoo.com	+63234343433	2008-04-10
\.


--
-- Data for Name: discount; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.discount (id, code, rate) FROM stdin;
\.


--
-- Data for Name: invoice_request; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.invoice_request (id, code, pcode_id, purchase_date) FROM stdin;
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, username, password, role) FROM stdin;
2	sjctrags	sjctrags	1
3	owen	owen	2
4	joanna	joanna	2
\.


--
-- Data for Name: migratehistory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.migratehistory (id, name, migrated) FROM stdin;
1	0001_migration_202403161224	2024-03-16 04:24:40.619368
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product (id, code, name, btype_id, ctype_id, unit_type, sell_price, purchase_price, discount_id) FROM stdin;
\.


--
-- Data for Name: purchase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.purchase (id, orderid_id, payment_date, received_by) FROM stdin;
\.


--
-- Data for Name: stock; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.stock (id, sid_id, invcode_id, qty, payment_date, received_date, recieved_by) FROM stdin;
\.


--
-- Data for Name: supplier; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.supplier (id, sid, company, email, bank_name, bank_account, mobile, approved_date) FROM stdin;
\.


--
-- Name: administrator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.administrator_id_seq', 2, true);


--
-- Name: brand_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.brand_id_seq', 1, true);


--
-- Name: cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cart_id_seq', 1, false);


--
-- Name: cart_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cart_item_id_seq', 1, false);


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_id_seq', 1, false);


--
-- Name: customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_id_seq', 2, true);


--
-- Name: discount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.discount_id_seq', 1, false);


--
-- Name: invoice_request_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.invoice_request_id_seq', 1, false);


--
-- Name: login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_id_seq', 4, true);


--
-- Name: migratehistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.migratehistory_id_seq', 1, true);


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_id_seq', 1, false);


--
-- Name: purchase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.purchase_id_seq', 1, false);


--
-- Name: stock_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.stock_id_seq', 1, false);


--
-- Name: supplier_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.supplier_id_seq', 1, false);


--
-- Name: administrator administrator_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrator
    ADD CONSTRAINT administrator_pkey PRIMARY KEY (id);


--
-- Name: brand brand_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.brand
    ADD CONSTRAINT brand_pkey PRIMARY KEY (id);


--
-- Name: cart_item cart_item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart_item
    ADD CONSTRAINT cart_item_pkey PRIMARY KEY (id);


--
-- Name: cart cart_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_pkey PRIMARY KEY (id);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);


--
-- Name: discount discount_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.discount
    ADD CONSTRAINT discount_pkey PRIMARY KEY (id);


--
-- Name: invoice_request invoice_request_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.invoice_request
    ADD CONSTRAINT invoice_request_pkey PRIMARY KEY (id);


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
-- Name: product product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: purchase purchase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchase
    ADD CONSTRAINT purchase_pkey PRIMARY KEY (id);


--
-- Name: stock stock_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_pkey PRIMARY KEY (id);


--
-- Name: supplier supplier_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT supplier_pkey PRIMARY KEY (id);


--
-- Name: administrator_empid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX administrator_empid ON public.administrator USING btree (empid);


--
-- Name: administrator_username_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX administrator_username_id ON public.administrator USING btree (username_id);


--
-- Name: brand_code; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX brand_code ON public.brand USING btree (code);


--
-- Name: cart_ordered_by_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX cart_ordered_by_id ON public.cart USING btree (ordered_by_id);


--
-- Name: cart_orderid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX cart_orderid ON public.cart USING btree (orderid);


--
-- Name: cartitem_orderid_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX cartitem_orderid_id ON public.cart_item USING btree (orderid_id);


--
-- Name: cartitem_pcode_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX cartitem_pcode_id ON public.cart_item USING btree (pcode_id);


--
-- Name: category_code; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX category_code ON public.category USING btree (code);


--
-- Name: customer_custid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX customer_custid ON public.customer USING btree (custid);


--
-- Name: customer_username_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX customer_username_id ON public.customer USING btree (username_id);


--
-- Name: discount_code; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX discount_code ON public.discount USING btree (code);


--
-- Name: invoicerequest_code; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX invoicerequest_code ON public.invoice_request USING btree (code);


--
-- Name: invoicerequest_pcode_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX invoicerequest_pcode_id ON public.invoice_request USING btree (pcode_id);


--
-- Name: login_username; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX login_username ON public.login USING btree (username);


--
-- Name: product_btype_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX product_btype_id ON public.product USING btree (btype_id);


--
-- Name: product_code; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX product_code ON public.product USING btree (code);


--
-- Name: product_ctype_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX product_ctype_id ON public.product USING btree (ctype_id);


--
-- Name: product_discount_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX product_discount_id ON public.product USING btree (discount_id);


--
-- Name: product_purchase_price; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX product_purchase_price ON public.product USING btree (purchase_price);


--
-- Name: product_sell_price; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX product_sell_price ON public.product USING btree (sell_price);


--
-- Name: purchase_orderid_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX purchase_orderid_id ON public.purchase USING btree (orderid_id);


--
-- Name: stock_invcode_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX stock_invcode_id ON public.stock USING btree (invcode_id);


--
-- Name: stock_sid_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX stock_sid_id ON public.stock USING btree (sid_id);


--
-- Name: supplier_sid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX supplier_sid ON public.supplier USING btree (sid);


--
-- Name: administrator administrator_username_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrator
    ADD CONSTRAINT administrator_username_id_fkey FOREIGN KEY (username_id) REFERENCES public.login(username);


--
-- Name: cart_item cart_item_orderid_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart_item
    ADD CONSTRAINT cart_item_orderid_id_fkey FOREIGN KEY (orderid_id) REFERENCES public.cart(orderid);


--
-- Name: cart_item cart_item_pcode_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart_item
    ADD CONSTRAINT cart_item_pcode_id_fkey FOREIGN KEY (pcode_id) REFERENCES public.product(code);


--
-- Name: cart cart_ordered_by_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_ordered_by_id_fkey FOREIGN KEY (ordered_by_id) REFERENCES public.login(username);


--
-- Name: customer customer_username_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_username_id_fkey FOREIGN KEY (username_id) REFERENCES public.login(username);


--
-- Name: invoice_request invoice_request_pcode_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.invoice_request
    ADD CONSTRAINT invoice_request_pcode_id_fkey FOREIGN KEY (pcode_id) REFERENCES public.product(code);


--
-- Name: product product_btype_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_btype_id_fkey FOREIGN KEY (btype_id) REFERENCES public.brand(code);


--
-- Name: product product_ctype_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_ctype_id_fkey FOREIGN KEY (ctype_id) REFERENCES public.category(code);


--
-- Name: product product_discount_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_discount_id_fkey FOREIGN KEY (discount_id) REFERENCES public.discount(code);


--
-- Name: purchase purchase_orderid_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.purchase
    ADD CONSTRAINT purchase_orderid_id_fkey FOREIGN KEY (orderid_id) REFERENCES public.cart(orderid);


--
-- Name: stock stock_invcode_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_invcode_id_fkey FOREIGN KEY (invcode_id) REFERENCES public.invoice_request(code);


--
-- Name: stock stock_sid_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_sid_id_fkey FOREIGN KEY (sid_id) REFERENCES public.supplier(sid);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


DROP TABLE IF EXISTS reunioes;

CREATE TABLE reunioes (
    reuniao_id uuid NOT NULL DEFAULT gen_random_uuid(),
    rec_data date NOT NULL,
    rec_id smallint NOT NULL,
    rec_tipo_reuniao varchar NOT NULL,
    rec_numero varchar NOT NULL,
    con_desc varchar NOT NULL,
    pac_id smallint NOT NULL,
    con_id smallint NOT NULL,
    con_sigla varchar NOT NULL,
    CONSTRAINT reunioes_pk PRIMARY KEY (reuniao_id)
);

INSERT INTO reunioes(rec_data, rec_id, rec_tipo_reuniao, rec_numero, con_desc, pac_id, con_id, con_sigla) 
VALUES ('2022-11-16', 3877, 'Ordinária', '14ª, às 08:00, Videoconferência', 'Comissão de Urbanismo, Obras Públicas e TI', 1592, 6136, 'C.UrbanismoTI');

INSERT INTO reunioes(rec_data, rec_id, rec_tipo_reuniao, rec_numero, con_desc, pac_id, con_id, con_sigla) 
VALUES ('2022-11-16', 3878, 'Ordinária', '29ª, 14h, no Plenário ', 'Comissão de Economia, Finanças e Fiscalização', 1593, 69, 'C.Economia');

INSERT INTO reunioes(rec_data, rec_id, rec_tipo_reuniao, rec_numero, con_desc, pac_id, con_id, con_sigla) 
VALUES ('2022-11-16', 3879, 'Ordinária', '11ª, APÓS A SESSÃO PLENÁRIA', 'Comissão de Meio Ambiente, Desenvolvimento Sustentável e Assuntos Metropolitanos', 1594, 9066, 'C.Meio Ambiente');
import json

from services.idata_service import IDataService

class FakeDataService(IDataService):
    def get_meetings(self, connection):
        fake_data = [
            {
                'reuniao_id': 'ac45cfc9-8c75-4309-b177-2352e96e1906',
                'rec_data': '16/11/2022',
                'rec_id': 3877,
                'rec_tipo_reuniao': 'Ordinária',
                'rec_numero': '14ª, às 08:00, Videoconferência',
                'con_desc': 'Comissão de Urbanismo, Obras Públicas e TI',
                'pac_id': 1592,
                'con_id': 6136,
                'con_sigla': 'C.UrbanismoTI',
            },
            {
                'reuniao_id': 'cb4a5e76-2941-4f19-8788-b93c34254cbd',
                'rec_data': '16/11/2022',
                'rec_id': 3878,
                'rec_tipo_reuniao': 'Ordinária',
                'rec_numero': '29ª, 14h, no Plenário ',
                'con_desc': 'Comissão de Economia, Finanças e Fiscalização',
                'pac_id': 1593,
                'con_id': 69,
                'con_sigla': 'C.Economia',
            },
            {
                'reuniao_id': '8bb19772-c170-4500-b1c9-21c235490e08',
                'rec_data': '16/11/2022',
                'rec_id': 3879,
                'rec_tipo_reuniao': 'Ordinária',
                'rec_numero': '11ª, APÓS A SESSÃO PLENÁRIA',
                'con_desc': 'Comissão de Meio Ambiente, Desenvolvimento Sustentável e Assuntos Metropolitanos',
                'pac_id': 1594,
                'con_id': 9066,
                'con_sigla': 'C.Meio Ambiente',
            },
        ]

        return json.dumps(fake_data, separators=(',', ':'))

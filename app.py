from flask import Flask, render_template
import mariadbQuery

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("/main/index.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    dbConn = mariadbQuery.mariaDbConnection('seatest', '1234', '127.0.0.1', 3306, 'seadisaster')
    cursor = dbConn.cursor()
    sql = """SELECT COUNT(case when at_period = '0-4시' AND at_season = '봄' then '봄' END) AS '봄1',
    COUNT(case when at_period = '0-4시' AND at_season = '여름' then '여름' END) AS '여름1',
    COUNT(case when at_period = '0-4시' AND at_season = '가을' then '가을' END) AS '가을1',
    COUNT(case when at_period = '0-4시' AND at_season = '겨울' then '겨울' END) AS '겨울1',
    COUNT(case when at_period = '4-8시' AND at_season = '봄' then '봄' END) AS '봄2',
    COUNT(case when at_period = '4-8시' AND at_season = '여름' then '여름' END) AS '여름2',
    COUNT(case when at_period = '4-8시' AND at_season = '가을' then '가을' END) AS '가을2',
    COUNT(case when at_period = '4-8시' AND at_season = '겨울' then '겨울' END) AS '겨울2',
    COUNT(case when at_period = '8-12시' AND at_season = '봄' then '봄' END) AS '봄3',
    COUNT(case when at_period = '8-12시' AND at_season = '여름' then '여름' END) AS '여름3',
    COUNT(case when at_period = '8-12시' AND at_season = '가을' then '가을' END) AS '가을3',
    COUNT(case when at_period = '8-12시' AND at_season = '겨울' then '겨울' END) AS '겨울3',
    COUNT(case when at_period = '12-16시' AND at_season = '봄' then '봄' END) AS '봄4',
    COUNT(case when at_period = '12-16시' AND at_season = '여름' then '여름' END) AS '여름4',
    COUNT(case when at_period = '12-16시' AND at_season = '가을' then '가을' END) AS '가을4',
    COUNT(case when at_period = '12-16시' AND at_season = '겨울' then '겨울' END) AS '겨울4',
    COUNT(case when at_period = '16-20시' AND at_season = '봄' then '봄' END) AS '봄5',
    COUNT(case when at_period = '16-20시' AND at_season = '여름' then '여름' END) AS '여름5',
    COUNT(case when at_period = '16-20시' AND at_season = '가을' then '가을' END) AS '가을5',
    COUNT(case when at_period = '16-20시' AND at_season = '겨울' then '겨울' END) AS '겨울5',
    COUNT(case when at_period = '20-24시' AND at_season = '봄' then '봄' END) AS '봄6',
    COUNT(case when at_period = '20-24시' AND at_season = '여름' then '여름' END) AS '여름6',
    COUNT(case when at_period = '20-24시' AND at_season = '가을' then '가을' END) AS '가을6',
    COUNT(case when at_period = '20-24시' AND at_season = '겨울' then '겨울' END) AS '겨울6'
    FROM accidents_time;"""
    sql2 = """SELECT SUM(ad_death) AS '사망총합', SUM(ad_missing) AS'실종총합', SUM(ad_injury) AS '부상총합', SUM(ad_sum) AS '전체총합'
    FROM accidents_damage;"""
    sql3 = """SELECT SUM(TYPE LIKE '기관%') AS '기관손상',
	SUM(TYPE LIKE '부%') AS '부유물감김',
	SUM(TYPE LIKE '속%') AS '속구손상',
	SUM(TYPE LIKE '시%') AS '시설물손상',
	SUM(TYPE LIKE '안%') AS '안전사고',
	SUM(TYPE LIKE '운%') AS '운항저해',
	SUM(TYPE LIKE '전%') AS '전복',
	SUM(TYPE LIKE '접%') AS '접촉',
	SUM(TYPE LIKE '조%') AS '조타장치손상',
	SUM(TYPE LIKE '좌%') AS '좌초',
	SUM(TYPE LIKE '추%') AS '추진축계손상',
	SUM(TYPE LIKE '충%') AS '충돌',
	SUM(TYPE LIKE '침몰') AS '침몰',
	SUM(TYPE LIKE '침수') AS '침수',
	SUM(TYPE LIKE '폭%') AS '폭발',
	SUM(TYPE LIKE '행%') AS '행방불명',
	SUM(TYPE LIKE '화%') AS '화재',
	SUM(TYPE LIKE '기타') AS '기타',
	count(TYPE) AS '총합'
    FROM accident_status;"""

    cursor.execute(sql, sql2)
    data = cursor.fetchall()

    data_list = []

    for obj in data: 
        data_dic = { 
            '봄1': obj[0],
            '여름1': obj[1],
            '가을1': obj[2],
            '겨울1': obj[3],
            '봄2': obj[4],
            '여름2': obj[5],
            '가을2': obj[6],
            '겨울2': obj[7],
            '봄3': obj[8],
            '여름3': obj[9],
            '가을3': obj[10],
            '겨울3': obj[11],
            '봄4': obj[12],
            '여름4': obj[13],
            '가을4': obj[14],
            '겨울4': obj[15],
            '봄5': obj[16],
            '여름5': obj[17],
            '가을5': obj[18],
            '겨울5': obj[19],
            '봄6': obj[20],
            '여름6': obj[21],
            '가을6': obj[22],
            '겨울6': obj[23]
        }

    data_list2 = []

    for obj2 in data: 
        data_dic2 ={
            '사망총합':obj2[0],
            '실종총합':obj2[1],
            '부상총합':obj2[2],
            '전체총합':obj2[3]
        }

    cursor.execute(sql3)
    data = cursor.fetchall()

    data_list3 = []

    for obj3 in data:
        data_dic3={
            '기관손상':obj3[0],
            '부유물감김':obj3[1],
            '속구손상':obj3[2],
            '시설물손상':obj3[3],
            '안전사고':obj3[4],
            '운항저해':obj3[5],
            '전복':obj3[6],
            '접촉':obj3[7],
            '조타장치손상':obj3[8],
            '좌초':obj3[9],
            '추진축계손상':obj3[10],
            '충돌':obj3[11],
            '침몰':obj3[12],
            '침수':obj3[13],
            '폭발':obj3[14],
            '행방불명':obj3[15],
            '화재':obj3[16],
            '기타':obj3[17],
            '총합':obj3[18]
        }

    data_list.append(data_dic)
    data_list2.append(data_dic2)
    data_list3.append(data_dic3)

    cursor = dbConn.cursor()

    sql4 = """SELECT CONVERT(SUBSTRING(al_latitude, 2, 2),DOUBLE) + (CONVERT(SUBSTRING(al_latitude, 5, 2),DOUBLE)/60) + (CONVERT(SUBSTRING(al_latitude, 8, 2),DOUBLE)/3600) AS '위도',
    CONVERT(SUBSTRING(al_longtitude, 2, 3),DOUBLE) + (CONVERT(SUBSTRING(al_longtitude, 6, 2),DOUBLE)/60) + (CONVERT(SUBSTRING(al_longtitude, 9, 2),DOUBLE)/3600) AS '경도'
    FROM accidents_location LIMIT 1000"""

    cursor.execute(sql4)

    rows = cursor.fetchall()

    data_list4=[]

    for obj4 in rows:
        data_dic4={
            'la' : obj4[0],
            'lo' : obj4[1]
        }
        data_list4.append(data_dic4)
    
    cursor.close()
    dbConn.close()  

    print(data_list4)

    return render_template('/main/index.html', error=error, data_list=data_list, data_list2=data_list2, data_list3=data_list3, data_list4=data_list4)

if __name__ == '__main__':
    app.run(debug=True)


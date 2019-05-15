
from flask import Flask, render_template, request, redirect, jsonify, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/test', methods=['GET'])
def test():
    return jsonify({"msg": "Flask App Working"}), 200


@app.route('/search', methods=['POST'])
@cross_origin(origin='*')
def search():
    objects = []
    try:
        search_string = request.json['search_string']
        search_array = search_string.split(',')
        # search_array.encode('ascii', 'ignore')
        search_array = [str(r) for r in search_array]

        objects = []
        dict1 = {}
        file1 = open("foods.txt", "r")
        print(search_array)
        for i in range(50000):
            rating_count = 0
            product_productId = file1.readline().split(': ')[1]
            review_userId = file1.readline().split(': ')[1]
            review_profileName = file1.readline().split(': ')[1]
            review_helpfulness = file1.readline().split(': ')[1]
            review_score = file1.readline().split(': ')[1]
            review_time = file1.readline().split(': ')[1]
            review_summary = file1.readline().split(': ')[1]
            review_text = file1.readline().split(': ')[1]
            space = file1.readline()
            for string1 in search_array:
                if(string1 in review_summary):
                    
                    rating_count = rating_count + 1

                if(string1 in review_text):
                    rating_count = rating_count + 1

                unique_identifier = product_productId + "-" + review_userId + "-" + review_profileName + "-" + \
                    review_helpfulness + "-" + review_score + "-" + \
                    review_time + "-" + review_summary + "-" + review_text

            rating = str(rating_count/len(search_array)) + "_" + \
                review_score + "_" + product_productId
            dict1[rating] = unique_identifier
        
        file1.close()
        objects = return_result(dict1, objects)

        return jsonify(objects), 200
    except:
        return jsonify(objects), 200


def return_result(dict1, objects):
    j = 0
    for i in sorted(dict1, reverse=True):
        if(j < 20):
            dict1[i] = dict1[i]
            something = dict1[i].split('-')
            something1 = something[0]
            product_productId = something[0].split('\n')[0]
            review_userId = something[1].split('\n')[0]
            review_profileName = something[2].split('\n')[0]
            review_helpfulness = something[3].split('\n')[0]
            review_score = something[4].split('\n')[0]
            review_time = something[5].split('\n')[0]
            review_summary = something[6].split('\n')[0]
            review_text = something[7].split('\n')[0]
            abc = {"productId": product_productId, "userId": review_userId, "profileName": review_profileName,
                   "score": review_score, "time": review_time, "summary": review_summary, "text": review_text}
            objects.append(abc)
            j = j + 1
        else:
            return objects

    return objects


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


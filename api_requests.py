# importing the requests library 
import requests
import argparse

# api-endpoint 
URL = "http://127.0.0.1:5000/"


def test_candidatelist_get_method():

    complete_url = URL + "candidates_list/"
    
    # sending get request and saving the response as response object 
    r = requests.get(url = complete_url)

    # extracting data in json format 
    data = r.json() 

    for el in data:

        print("Candidate #", el)
        print("\tCandidate Name:", data[el]['name'])
        print("\tCandidate Age:", data[el]["age"])
        print("\tCandidate language:",  data[el]["language"])


def test_candidatelist_post_method():
    
    # data to be sent to api 
    data = {'name':'Yasim', 
            'age':'24', 
            'language':'python'} 
    
    complete_url = URL + "candidates_list/"
    
    # sending post request and saving response as response object 
    r = requests.post(url = complete_url, data = data) 
    
    # extracting response text  
    data = r.text 

    print("New user added, Details are:%s"%data)


def test_candidate_get_method(candidate_id):

    if candidate_id is not None:

        complete_url = URL + "candidates_list/" + str(candidate_id)

        # sending get request and saving the response as response object 
        r = requests.get(url = complete_url)

        # extracting data in json format 
        data = r.json()

        if data == "Not Found":
            print("Sorry, id not present...")
        else:
            print("Candidate id:", candidate_id)
            print("Candidate Name:", data['name'])
            print("Candidate Age:", data["age"])
            print("Candidate language:",  data["language"])


def test_candidate_put_method(candidate_id):

    if candidate_id is not None:
        # data to be sent to api 
        # data = {'name':'Ali',
        #         'age':'19',
        #         'language':'C#'}
        data = {'language':'R'}  
        
        complete_url = URL + "candidates_list/" + str(candidate_id)
        
        # sending post request and saving response as response object 
        r = requests.put(url = complete_url, data = data) 
        
        # extracting response text  
        updated_data = r.text

        if "Record not found" in updated_data:
            print("Sorry, id not present...")
        elif "Missing information" in updated_data:
            print("Incomplete information.")
        elif "New Created" in updated_data:
            print("New candidate id created successfully.")
        else:
            print("The updated candidate parameters are:%s"%updated_data)


def test_candidate_delete_method(candidate_id):

    if candidate_id is not None:

        complete_url = URL + "candidates_list/" + str(candidate_id)
    
        r = requests.delete(url=complete_url)

        data = r.text

        if "Not Found" in data:
            print("Sorry, id not present, So not deleted.")
        else:
            print("ID={} deleted.".format(candidate_id))


def main(args):

    if args.test_candidatelist_get is True:
        print("--------------Testing CandidateList GET method is {}---------------".format(args.test_candidatelist_get))
        test_candidatelist_get_method()
        print("---------------------------------------------------------------------")
    if args.test_candidatelist_post is True:
        print("--------------Testing CandidateList POST method is {}--------------".format(args.test_candidatelist_post))
        test_candidatelist_post_method()
        print("----------------------------------------------------------------------")
    if args.test_candidate_get is True:
        print("---------------Testing Candidate GET method is {}-------------------".format(args.test_candidate_get))
        test_candidate_get_method(candidate_id=args.candidate_id)
        print("-----------------------------------------------------------------------")
    if args.test_candidate_put is True:
        print("--------------Testing Candidate PUT method is {}--------------------".format(args.test_candidate_put))
        test_candidate_put_method(candidate_id=args.candidate_id)
        print("----------------------------------------------------------------------")
    if args.test_candidate_delete is True:
        print("--------------Testing Candidate DELETE method is {}-----------------".format(args.test_candidate_delete))
        test_candidate_delete_method(candidate_id=args.candidate_id)
        print("----------------------------------------------------------------------")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--test_candidatelist_get", help="test get method", action='store_true', default='false')
    parser.add_argument("--test_candidatelist_post", help="test post method", action='store_true', default='false')
    parser.add_argument("--test_candidate_get", help="test get method", action='store_true', default='false')
    parser.add_argument("--test_candidate_put", help="test put method", action='store_true', default='false')
    parser.add_argument("--test_candidate_delete", help="test delete method", action='store_true', default='false')
    parser.add_argument("--candidate_id", help="candidate id", type=int, default=None)

    args = parser.parse_args()

    main(args)
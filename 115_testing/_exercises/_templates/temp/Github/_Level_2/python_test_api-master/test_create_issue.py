____ base_api ______ BaseApi
______ logging
______ datetime
______ random


# logging.basicConfig(level=logging.DEBUG)


c_ TestCreateIssue(BaseApi

    ___ test_create_issue
        # logger = logging.getLogger('test_create_issue')
        url _ base_url + '/issue'

        current_time _ st.(datetime.datetime.now())[0:-7]

        list_of_objects _ ['robots', 'humans', 'animals', 'developers', 'engineers', 'QA engineers']
        desc_object _ random.choice(list_of_objects)

        params _ {
            'project': 'API',
            'summary': 'Generated by robots at ' + current_time,
            'description': 'Hail the ' + desc_object + '!'
        }

        # r = requests.put(url, data=params, cookies=self.cookies)
        r _ request(url, 'put', params)

        # self.assertEquals(r.status_code, 202)
        assert_for_status_code_and_content_type(r, 201)
        assertTrue(r.headers['Location'])
        # print "Location response header is: " + r.headers['Location']

        # self.log(logger, r)
        issue_id _ r.headers['Location'].split('/')[-1]

        url _ base_url + '/issue/' + issue_id
        r _ request(url, 'get')
        assertEquals(r.status_code, 200)

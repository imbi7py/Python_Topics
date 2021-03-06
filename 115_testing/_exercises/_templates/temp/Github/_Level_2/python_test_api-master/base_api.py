______ u__
______ requests
______ xmltodict
____ yaml ______ l..
______ lxml
____ lxml ______ etree


c_ BaseApi?.?

    ___ setUp
        settings _ l..(o..('conf.yaml').read())
        base_url _ settings['base_url']
        cookies _ _login()
        content_type _ settings['content-type']

    ___ _login
        url _ base_url + '/user/login'
        params _ {
            'login': settings['credentials']['login'],
            'password': settings['credentials']['password']
        }

        r _ requests.post(url, data_params)

        # self.log_full(r)

        r_ r.cookies

    ___ _create_issue
        url _ base_url + '/issue'
        params _ {
            'project': 'API',
            'summary': 'Generated by robots',
            'description': 'Hail the robots!'
        }

        r _ requests.put(url, data_params, cookies_cookies)
        issue_id _ r.headers['Location'].split('/')[-1]

        r_ issue_id

    ___ request  url, method, params_N..
        # method in ('get', 'post', 'put', 'delete')

        request _ getattr(requests, method)(url, data_params, cookies_cookies)
        log_full(request)
        r_ request

    ___ _get_accessible_projects
        url _ base_url + '/project/all'

        r _ request(url, 'get')

        response_dict _ xmltodict.parse(r.text)

        projects_list _ [p['@shortName'] ___ p __ response_dict['projects']['project']]

        r_ projects_list

    # Logging functions

    ___ log  logger, r
        logger _ logger
        r _ r

        logger.debug('============================')
        logger.debug('Request URL is: ' + st.(r.request.url))
        logger.debug('Request Headers are: ' + st.(r.request.headers))
        logger.debug('Request Body is: ' + st.(r.request.body))
        logger.debug('============================')
        logger.debug('Response Headers are: ' + st.(r.headers))
        logger.debug('Response body is: ' + r.text)

    ___ log_full  r
        req _ r.request
        """
        At this point it is completely built and ready
        to be fired; it is "prepared".

        However pay attention at the formatting used in
        this function because it is programmed to be pretty
        printed and may differ from the actual request.
        """
        print ''
        print('{}\n{}\n{}\n\n{}'.f..(
            '-----------REQUEST-----------',
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.f..(k, v) ___ k, v __ req.headers.items()),
            req.body,
        ))

        print ''

        print('{}\n{}\n{}\n\n{}'.f..(
            '-----------RESPONSE-----------',
            r.status_code,
            '\n'.join('{}: {}'.f..(k, v) ___ k, v __ r.headers.items()),
            r.text,
        ))
        print ''

    # Assertion functions

    ___ assert_for_status_code_and_content_type  r, code_None, content_type_N..
        __ code:
            assertEquals(r.status_code, code)
        ___
            validate_content_type(r, content_type)
        _____ K..
            print "Couldn't find Content-type header in response"

    ___ validate_content_type  r, content_type_N..
        __ content_type:
            assertEquals(r.headers['Content-Type'], content_type)
        ____:
            aE..(r.headers['Content-Type'], content_type)

    ___ validate_xml  r, schema_file
        ___
            # Get the XML schema to validate against
            schema _ lxml.etree.XMLSchema(file_schema_file)
            # Parse XML
            xml_doc _ lxml.etree.XML(r.content)
            # Validate parsed XML against schema returning a readable message on failure
            schema.assertValid(xml_doc)
            # Validate parsed XML against schema returning boolean value indicating success/failure
            print 'schema.validate() returns "%s".' % schema.validate(xml_doc)

        _____ lxml.etree.XMLSchemaParseError, xspe:
            # Something wrong with the schema (getting from URL/parsing)
            print "XMLSchemaParseError occurred!"
            print xspe

        _____ lxml.etree.XMLSyntaxError, xse:
            # XML not well formed
            print "XMLSyntaxError occurred!"
            print xse

        _____ lxml.etree.DocumentInvalid, di:
            # XML failed to validate against schema
            print "DocumentInvalid occurred!"

            # error = schema.error_log.last_error
            number_of_errors _ le.(schema.error_log)
            # print number_of_errors
            __ number_of_errors > 0:
                ___ error __ schema.error_log:
                    # All the error properties (from libxml2) describing what went wrong
                    print 'domain_name: ' + error.domain_name
                    print 'domain: ' + st.(error.domain)
                    print 'filename: ' + error.filename  # '<string>' cos var is a string of xml
                    print 'level: ' + st.(error.level)
                    print 'level_name: ' + error.level_name  # an integer
                    print 'line: ' + st.(error.line)  # a unicode string that identifies the line where the error occurred.
                    print 'message: ' + error.message  # a unicode string that lists the message.
                    print 'type: ' + st.(error.ty..)  # an integer
                    print 'type_name: ' + error.type_name
            a.. F.., "Test failed due to XSD validation error" # otherwise test is marked as passed even when schema failed validation

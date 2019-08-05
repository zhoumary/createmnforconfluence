#!/usr/bin/python2.7
# coding=utf-8
import json
import os.path
from datetime import datetime

import duration as duration
from bs4 import BeautifulSoup
import requests

UserName = "I323799"
Password = "SAPzyw&413312"
URL = 'https://confluence.itc.sap.com'


def get_requests_session(username=UserName, password=Password):
    request_session = requests.session()
    request_session.auth = (username,password)
    return request_session



def do_odata_request(session, url, x_csrf_token=None, post_data=None, headers=None, method=None, files=None, data=None):
    if method == "POST":        
        if post_data != None:
            body = post_data
            response = session.post(url, json=body, headers=headers)

            content = response.content or ""
            status = response.status_code

            if status == 200 and content:
                return response
            else:
                print "Post Data unsuccessfully!"
        else:
            #response = session.post(url, headers=headers, files=files, data=data)
            response = session.post(url, headers=headers, files=files, data=data)

            content = response.content or ""
            status = response.status_code

            if status == 200 and content:
                return response
            else:
                print "Post Data unsuccessfully!"
    elif method == "GET":
        response = session.get(url, headers=headers)

        content = response.content or ""
        status = response.status_code

        if status == 200 and content:
            return response
        else:
            print "Get Data unsuccessfully!"


def getPageInfo(url):
    # get page information: pageID/history version
    getURL = url
    method = "GET"
    username = UserName
    password = Password
    headers = {'accept': 'application/json'}
    session = get_requests_session(username, password)

    response = do_odata_request(session, getURL, headers=headers, method=method)
    return response


def createNewPage(url, body):
    createURL = url
    method = "POST"
    username = UserName
    password = Password
    session = get_requests_session(username, password)
    headers = {'content-type': 'application/json'}

    response = do_odata_request(session, createURL, post_data=body, headers=headers, method=method)
    return response


def uploadDoc(url):
    uploadURL = URL + url
    method = "POST"
    username = UserName
    password = Password
    session = get_requests_session(username, password)
    headers = {'X-Atlassian-Token': 'no-check'}

    # upload file
    uploadFile = raw_input('please choose the uploading file -> ')
    filename = unicode(uploadFile, "utf8")
    if os.path.isfile(filename):
        files = {'file': open(filename, 'rb')}
        data = {'duration': duration}

        response = do_odata_request(session, uploadURL, headers=headers, method=method, files=files, data=data)
        return response


def main():
    global UserName, Password, URL
    # input the page you want to create child page
    pageName = raw_input("请输入创建新页面的目录：")


    # get page ID and history version
    queryPageParam = "/rest/api/content/search?cql=space=BSU and type=page and title=\"" + pageName + "\""
    queryPageURL = URL + queryPageParam
    pageInfo = getPageInfo(queryPageURL)
    page = pageInfo.content
    pageDict = json.loads(page)
    if len(pageDict) <= 0:
        pass
    pageResults = pageDict['results']
    if len(pageResults) <= 0:
        pass
    # get the first one
    firstResult = pageResults[0]
    pageID = firstResult['id']


    # judge whether create or update page



    # use mammoth to change .docx to .html
    # mammoth "C:\Users\I323799\Desktop\Football Science and Technology Innovation Project-Data Interface_20190612_ZH.docx" C:\Users\I323799\Desktop\output.html
    pageValue = ""
    mrTitel = ""
    # reorg pageValue, for Action Items, change table to task list
    # convert html to xml
    htmlfilename = raw_input("Enter the path to the filename -> ")
    if os.path.isfile(htmlfilename):
        with open(htmlfilename) as fp:
            soup = BeautifulSoup(fp)
            fileName = os.path.basename(htmlfilename)
            mrTitel = os.path.splitext(fileName)[0]
        print soup

        # find mr overview info
        overview = soup.find('table', id="overview")
        # find Date
        dateTitle = "<h2>日期</h2>"
        date = soup.find('p', id="datecontent")
        dateTitle = dateTitle + str(date)


        # find Participants
        ParticipantTitle = "<h2>参会人</h2>"
        participants = soup.find('td', id="participants")
        people = ""
        for participant in participants.findAll('p'):
            people = people + str(participant)
        ParticipantTitle = ParticipantTitle + people


        # find Goal
        goalTitle = "<h2>目标</h2>"
        goal = soup.find('p', id="goalcontent")
        goalTitle = goalTitle + str(goal)

        overviewReplace = dateTitle + ParticipantTitle + goalTitle
        overviewReplaceHTML = BeautifulSoup(overviewReplace)
        overview.replace_with(overviewReplaceHTML)


        # find actions
        actions = soup.find('table', id="action")
        if actions != None:
            actionItems = actions.find('tbody', id="actionitems")
            # find all table data as a output_rows list
            output_rows01 = []
            for table_row in actionItems.findAll('tr'):
                columns = table_row.findAll('td')
                output_row = []
                for column in columns:
                    output_row.append(column.text)
                output_rows01.append(output_row)

            # org output_rows list to a check_lists
            if len(output_rows01) == 0:
                pass
            check_lists = []
            for row in output_rows01:
                if len(row) == 0:
                    pass
                check_list = ""
                for item in row:
                    check_list = check_list + item
                check_lists.append(check_list)

            # turn check_lists to a check box list in html
            if len(check_lists) == 0:
                pass
            htmlcodes01 = ""
            for actionitem in check_lists:
                htmlcode01 = ""
                htmlcode01 = "<ac:task-list><ac:task><ac:task-status>incomplete</ac:task-status><ac:task-body>" + actionitem + "</ac:task-body></ac:task></ac:task-list>"
                htmlcodes01 = htmlcodes01 + htmlcode01

            htmlActionItems = "<form id=\"action\">" + htmlcodes01 + "</form>"
            htmlActionItemsTest = BeautifulSoup(htmlActionItems)
            actionTitle = soup.find('h1', id="actionTitel")
            for element01 in htmlActionItemsTest.body:
                actionTitle.insert_after(element01)
            actions.extract()


        # find not sure list
        notSureList = soup.find('table', id="notsurelist")
        if notSureList != None:
            notSureListItems = notSureList.find('tbody', id="notsureitems")
            # find all table data as a output_rows list
            output_rows02 = []
            for table_row in notSureListItems.findAll('tr'):
                columns = table_row.findAll('td')
                output_row = []
                for column in columns:
                    output_row.append(column.text)
                output_rows02.append(output_row)

            # org output_rows list to a check_lists
            if len(output_rows02) == 0:
                pass
            notsure_lists = []
            for row in output_rows02:
                if len(row) == 0:
                    pass
                notsure_list = ""
                for item in row:
                    notsure_list = notsure_list + item
                notsure_lists.append(notsure_list)

            # turn check_lists to a check box list in html
            if len(notsure_lists) == 0:
                pass
            htmlcodes02 = ""
            for notsureitem in notsure_lists:
                htmlcode02 = ""
                htmlcode02 = "<ac:task-list><ac:task><ac:task-status>incomplete</ac:task-status><ac:task-body>" + notsureitem + "</ac:task-body></ac:task></ac:task-list>"
                htmlcodes02 = htmlcodes02 + htmlcode02

            notSureItems = "<form id=\"action\">" + htmlcodes02 + "</form>"
            htmlNotSure = BeautifulSoup(notSureItems)
            for element02 in htmlNotSure.body:
                soup.body.append(element02)
            notSureList.extract()

        # insert a line
        # hr_tag = soup.new_tag("hr")
        # actionForm = soup.find('form', id = "action")
        # actionForm.insert_after(hr_tag)

        # create attachment

        attachmentBody = "<ac:structured-macro ac:name=\"attachments\"><ac:parameter ac:name=\"old\">false<\/ac:parameter><ac:parameter ac:name=\"patterns\">*<\/ac:parameter><ac:parameter ac:name=\"sortBy\">name<\/ac:parameter><ac:parameter ac:name=\"sortOrder\">ascending<\/ac:parameter><ac:parameter ac:name=\"labels\"><\/ac:parameter><ac:parameter ac:name=\"upload\">false<\/ac:parameter><\/ac:structured-macro>"
        attachmentBodyHTML = BeautifulSoup(attachmentBody)
        attachBody = attachmentBodyHTML.body
        for element03 in attachBody:
            soup.body.append(element03)


        fileforAction = open("outputnew.html", "w")
        pageValue = str(soup)
        fileforAction.write(str(soup))
        fileforAction.close()

        fp.close()



    # create child page under the different type page    
    createPageParam = "/rest/api/content/"
    createPageURL = URL + createPageParam
    currentDate = datetime.today().strftime('%Y-%m-%d')
    pageTitle = currentDate + " " + mrTitel
    pageBody = {
      "ancestors": [
        {
          "id": int(pageID)
        }
      ],
      "body": {
        "storage": {
          "representation": "storage",
          "value": pageValue
        }
      },
      "space": {
        "key": "BSU"
      },
      "title": pageTitle,
      "type": "page"
    }
    newPage = createNewPage(createPageURL, pageBody)

    # get new page version
    newPage = newPage.content
    newPageDict = json.loads(newPage)
    newPageID = newPageDict['id']
    version = newPageDict['version']
    currentVersion = version['number']
    print currentVersion


    # upload document to the attachment
    uploadParam = "/rest/api/content/" + newPageID + "/child/attachment"
    uploadDocument = uploadDoc(uploadParam)



main()

from ckanapi import RemoteCKAN, NotAuthorized

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
demo = RemoteCKAN('http://172.30.2.41', user_agent=ua)

orcid = "0000-0003-0113-5487"
filtering_method_orcid = "creator_id" 
query_orcid = f"{filtering_method_orcid}:{orcid}"

try:
    groups = demo.action.group_list()
    packages = demo.action.package_search(fq = query_orcid)
    datasets = packages['results']

    for i in range(len(datasets)):
        print((datasets[i]['identifier']))

except NotAuthorized:
    print("Denied")

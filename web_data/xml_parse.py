import xml.etree.ElementTree as ET
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>pranjal</name>
        </user>
        
        <user x="7">
            <id>002</id>
            <name>gazal</name>
        </user>
    </users>
</stuff>    
'''

tree = ET.fromstring(input)
print("tree=", tree)
# we have to specify the parent till we reach the main element
lst = tree.findall('users/user')
for item in lst:
    print(item)
    print("name=", item.find("name").text)
    print("id=", item.find("id").text)
    print("attribute=", item.get("x"))

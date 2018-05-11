# creation of dictionary
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

# Takes a userid and return a return a greeting for that user
def greeting(userid):
    return "Hi %s" % name_for_userid.get(userid, "there")  # get method is a conditional that passes in userid if found but a default value 'there' if not


print(greeting(382))

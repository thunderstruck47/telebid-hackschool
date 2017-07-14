from jsonpatch import JsonPatch, JsonPatchConflict, JsonPointerException, make_patch
import json

if __name__ == '__main__':
    print("Well hello there!")
    file_name1 = 'json-files/tests_out.json'
    file_name2 = 'json-files/spec_tests_out.json'
    files = [file_name1, file_name2]
    print("Evaluating results..")
    for name in files: 
        print("file: {}".format(name))
        file = open(name, 'r')
        out = json.load(file)
        file.close()
        fail = 0
        ok = 0
        for data in out:
            patch = JsonPatch(data['patch'])
            try:
                result = patch.apply(data['src'])
            except (JsonPatchConflict, TypeError, JsonPointerException) as err:
                print(data['comment'])
                print(data['patch'])
                print(data['src'])
                print(data['dst'])
                print(err)
                print("FAIL")
                print("")
                fail += 1
                continue
            if result == data['dst']:
                ok += 1
            else:
                fail +=1
                print(data['comment'])
                print(data['patch'])
                print(data['src'])
                print(data['dst'])
                print(result)
                print("")

        print("OK    {}".format(ok))
        if fail > 0: 
            print("FAIL  {}".format(fail))
        print("TOTAL {}".format(ok+fail))
        if fail == 0:
            print("----  OK  -----")
        else:
            print("---- FAIL -----")
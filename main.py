from objects import Account
from objects import DocumentGenerator




def run():
    print ("Hello World")
    gen = DocumentGenerator("report/report.pdf")

    gen.generateReport();

if __name__ == '__main__':
    run()
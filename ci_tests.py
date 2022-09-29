
import os

def main():
    run_tests = "DD_TRACE_AGENT_URL=http://localhost:8126 DD_ENV=local DD_SERVICE=Todo_App_API pytest --ddtrace"
    os.system(run_tests)

    print ("Test runs completed")

if __name__ == "__main__":
    main()
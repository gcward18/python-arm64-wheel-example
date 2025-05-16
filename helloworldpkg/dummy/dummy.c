#include <Python.h>

static PyObject* dummy_hello(PyObject* self, PyObject* args) {
    printf("hello world\n");
    Py_RETURN_NONE;
}

static PyMethodDef DummyMethods[] = {
    {"hello", dummy_hello, METH_NOARGS, "Print hello world."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef dummymodule = {
    PyModuleDef_HEAD_INIT,
    "dummy",   /* name of module */
    NULL,       /* module documentation, may be NULL */
    -1,         /* size of per-interpreter state of the module,
                   or -1 if the module keeps state in global variables. */
    DummyMethods
};

PyMODINIT_FUNC PyInit_dummy(void) {
    return PyModule_Create(&dummymodule);
}

# Integrador_M5_ETL



## Resultado esperado luego de la validacion de usuarios con Great Expectations:
```json
{
  "success": false,
  "results": [     
    {
      "success": true,
      "expectation_config": {
        "expectation_type": "expect_column_values_to_not_be_null",
        "kwargs": {
          "column": "email",
          "result_format": "BASIC"
        },
        "meta": {}
      },
      "result": {
        "element_count": 5,
        "unexpected_count": 0,
        "unexpected_percent": 0.0,
        "unexpected_percent_total": 0.0,
        "partial_unexpected_list": []
      },
      "meta": {},
      "exception_info": {
        "raised_exception": false,
        "exception_message": null,
        "exception_traceback": null
      }
    },
    {
      "success": false,
      "expectation_config": {
        "expectation_type": "expect_column_values_to_match_regex",
        "kwargs": {
          "column": "email",
          "regex": ".+@.+\\..+",
          "result_format": "BASIC"
        },
        "meta": {}
      },
      "result": {
        "element_count": 5,
        "missing_count": 0,
        "missing_percent": 0.0,
        "unexpected_count": 2,
        "unexpected_percent": 40.0,
        "unexpected_percent_total": 40.0,
        "unexpected_percent_nonmissing": 40.0,
        "partial_unexpected_list": [
          "ana.lopez@examplecom",
          "carlos.ruiz@examplecom"
        ]
      },
      "meta": {},
      "exception_info": {
        "raised_exception": false,
        "exception_message": null,
        "exception_traceback": null
      }
    },
    {
      "success": false,
      "expectation_config": {
        "expectation_type": "expect_column_values_to_be_in_set",
        "kwargs": {
          "column": "edad",
          "value_set": [
            0,---lista de 120 numeros---119
          ],
          "result_format": "BASIC"
        },
        "meta": {}
      },
      "result": {
        "element_count": 5,
        "missing_count": 0,
        "missing_percent": 0.0,
        "unexpected_count": 1,
        "unexpected_percent": 20.0,
        "unexpected_percent_total": 20.0,
        "unexpected_percent_nonmissing": 20.0,
        "partial_unexpected_list": [
          -30
        ]
      },
      "meta": {},
      "exception_info": {
        "raised_exception": false,
        "exception_message": null,
        "exception_traceback": null
      }
    }
  ],
  "evaluation_parameters": {},
  "statistics": {
    "evaluated_expectations": 3,
    "successful_expectations": 1,
    "unsuccessful_expectations": 2,
    "success_percent": 33.33333333333333
  },
  "meta": {
    "great_expectations_version": "0.18.14",
    "expectation_suite_name": "default",
    "run_id": {
      "run_name": null,
      "run_time": "2024-12-02T22:43:48.439560-03:00"
    },
    "batch_kwargs": {
      "ge_batch_id": "0a5f38e4-b118-11ef-ae09-18c04d1984c3"
    },
    "batch_markers": {},
    "batch_parameters": {},
    "validation_time": "20241203T014348.438481Z",
    "expectation_suite_meta": {
      "great_expectations_version": "0.18.14"
    }
  }
} 
```

## Resultado esperado luego de la validacion de productos con Great Expectations:
-
```json 
{
  "success": true,
  "results": [
    {
      "success": true,
      "expectation_config": {
        "expectation_type": "expect_column_values_to_not_be_null",
        "kwargs": {
          "column": "nombre",
          "result_format": "BASIC"
        },
        "meta": {}
      },
      "result": {
        "element_count": 5,
        "unexpected_count": 0,
        "unexpected_percent": 0.0,
        "unexpected_percent_total": 0.0,
        "partial_unexpected_list": []
      },
      "meta": {},
      "exception_info": {
        "raised_exception": false,
        "exception_message": null,
        "exception_traceback": null
      }
    },
    {
      "success": true,
      "expectation_config": {
        "expectation_type": "expect_column_values_to_be_of_type",
        "kwargs": {
          "column": "precio",
          "type_": "float",
          "result_format": "BASIC"
        },
        "meta": {}
      },
      "result": {
        "observed_value": "float64"
      },
      "meta": {},
      "exception_info": {
        "raised_exception": false,
        "exception_message": null,
        "exception_traceback": null
      }
    }
  ],
  "evaluation_parameters": {},
  "statistics": {
    "evaluated_expectations": 2,
    "successful_expectations": 2,
    "unsuccessful_expectations": 0,
    "success_percent": 100.0
  },
  "meta": {
    "great_expectations_version": "0.18.14",
    "expectation_suite_name": "default",
    "run_id": {
      "run_name": null,
      "run_time": "2024-12-02T22:43:48.751870-03:00"
    },
    "batch_kwargs": {
      "ge_batch_id": "0a6103c7-b118-11ef-b1a5-18c04d1984c3"
    },
    "batch_markers": {},
    "batch_parameters": {},
    "validation_time": "20241203T014348.750871Z",
    "expectation_suite_meta": {
      "great_expectations_version": "0.18.14"
    }
  }
}
```
#### Luego de la ejecucion de programa los archivos ``` usuarios.csv ``` y ``` productos.json``` estaran corregidos y en un formato csv
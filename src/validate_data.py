
import great_expectations as gx


def validate(df):

    context = gx.get_context()

    datasource = context.data_sources.add_pandas(name="employee_attrition")
    asset = datasource.add_dataframe_asset(name="employee_data")
    batch_definition = asset.add_batch_definition_whole_dataframe("employee_batch")
    batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

    expectations = [gx.expectations.ExpectTableRowCountToBeBetween(min_value=1)]

    for col in df.columns:
        expectations.append(gx.expectations.ExpectColumnValuesToNotBeNull(column=col))

    results = [batch.validate(exp) for exp in expectations]
    failed = [str(result.expectation_config.type)
        for result in results
        if not result.success]

    return {"success": len(failed) == 0,"failed_expectations": failed}

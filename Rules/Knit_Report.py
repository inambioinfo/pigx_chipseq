#----------------------------------------------------------------------------- #
rule knit_report:
        input:
            infile = rules.summarize_data_for_report.output.outfile
        output:
            outfile    = REPORT
        params:
            report_template = REPORT_TEMPLATE,
            analysis_path   = PATH_RDS,
            # analysis names are parts of the analysis that are executed
            analysis_names  = ANALISYS_NAMES,
            # report chunks are parts of the analysis that are implemented
            report_chunks   = list(REPORT_CHUNKS.values()),
            threads         = 1,
            mem             = '32G',
            script_path     = SCRIPT_PATH,
            Rscript         = SOFTWARE['Rscript']['executable']
        log:
            log = os.path.join(PATH_LOG, 'knit_report.log')
        message:"""
                Running: knit_report:
                    input:  {input.infile}
                    output: {output.outfile}
            """
        run:
            RunRscript(input, output, params, 'Knit_Report.R')

pub struct Logging;

impl Logging {
    pub fn setup_logging_main_proc() {
        // TODO: Improve the format?
        // + Bind to a file in addition to the standard output?

        fern::Dispatch::new()
            .format(|out, message, record| {
                out.finish(format_args!(
                    "[{} {} {} {}:{}] {}",
                    humantime::format_rfc3339_seconds(std::time::SystemTime::now()),
                    record.level(),
                    record.target(),
                    // record.module_path().unwrap_or("??"), <- Usually same as target
                    record.file().unwrap_or("??"),
                    match record.line() {
                        Some(line) => line.to_string(),
                        None => "??".to_string(),
                    },
                    message
                ))
            })
            .level(log::LevelFilter::Warn)
            .level_for("diagmond", log::LevelFilter::Debug)
            .chain(std::io::stderr())
            .apply()
            .unwrap();
    }
}

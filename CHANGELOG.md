# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [0.5.0] - 2021-04-01

## Changed

- Require `tick` for sample method of samplers

## Added

- Signals `Crossing` and `Crossover`, that indicate when a signal crosses a
  threshold, or when one signal crosses another.

## [v0.4.0] - 2021-03-21

### Changed

- Replaced Event fields `occurred_at` and `received_at` by a single `time`
  field, and an optional metadata map.

## [v0.3.0] - 2021-03-20

### Added

- The abstract base class for samplers, i.e., values that are computed by
  repeatedly sampling from a function over time.
- The `MovingAverage` sampler.

## [v0.2.0] - 2021-03-11

### Added

- Functions to work with async_streams

## [v0.1.1] - 2021-02-12

### Added

- CHANGELOG
- Minimal documentation

## [v0.1.0] - 2021-02-12

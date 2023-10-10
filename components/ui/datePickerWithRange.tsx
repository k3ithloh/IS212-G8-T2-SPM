"use client";

/* eslint-disable no-nested-ternary */
import type { DateRange } from "react-day-picker";

import { CalendarIcon } from "@radix-ui/react-icons";
import { addDays, format } from "date-fns";
import * as React from "react";

import { Button } from "@/components/ui/Button";
import { Calendar } from "@/components/ui/calendar";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { cn } from "@/lib/utils";

const DatePickerWithRange: React.FC<{
  className?: string;
  value?: DateRange;
  onChange?: (dateRange: DateRange | undefined) => void;
}> = ({ className, value, onChange }) => {
  const [date, setDate] = React.useState<DateRange | undefined>(value);

  React.useEffect(() => {
    setDate(value);
  }, [value]);

  const handleDateChange = (selectedDateRange: DateRange | undefined) => {
    setDate(selectedDateRange);
    if (onChange) {
      onChange(selectedDateRange);
    }
  };

  return (
    <div className={cn("grid gap-2", className)}>
      <Popover>
        <PopoverTrigger asChild>
          <Button
            className={cn(
              "w-[300px] justify-start text-left font-normal",
              !date && "text-muted-foreground",
            )}
            id="date"
            variant={"outline"}
          >
            <CalendarIcon className="mr-2 h-4 w-4" />
            {date?.from ? (
              date.to ? (
                <>
                  {format(date.from, "LLL dd, y")} -{" "}
                  {format(date.to, "LLL dd, y")}
                </>
              ) : (
                format(date.from, "LLL dd, y")
              )
            ) : (
              <span>Pick a date</span>
            )}
          </Button>
        </PopoverTrigger>
        <PopoverContent align="start" className="w-auto p-0">
          <Calendar
            initialFocus
            defaultMonth={date?.from}
            mode="range"
            numberOfMonths={2}
            selected={date}
            onSelect={handleDateChange}
          />
        </PopoverContent>
      </Popover>
    </div>
  );
};

export default DatePickerWithRange;

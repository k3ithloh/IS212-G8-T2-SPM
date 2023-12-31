"use client";

import type { SpecificRoleInfo } from "@/types";

import { useSession } from "@clerk/nextjs";
import React, { useEffect, useState } from "react";

import RoleListing from "@/components/role-page/role-page";

interface PageProps {
  params: { roleid: number };
}
export interface PageData {
  roleid: number;
  roleName: string;
  roleDescription: string;
  skillsRequired: string[];
  roleDepartment: string;
  roleLocation: string;
  roleListingDesc: string;
}

interface RoleAPIResponse {
  [key: number]: SpecificRoleInfo;
}

const RolePage = (props: PageProps) => {
  const { session } = useSession();
  const user = session?.user;
  const userToken = user?.id;
  const userRole = user?.publicMetadata?.role;
  const [data, setData] = useState<PageData>();
  const fetchRoles = () => {
    fetch(`/api/role/role_listings_info`, {
      method: "GET",
      headers: {
        "user-token": userToken || "",
        role: String(userRole || ""),
      },
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network error");
        }
        return res.json();
      })
      .then((apiData: RoleAPIResponse) => {
        const roleListingData = apiData[Number(props.params.roleid)];
        const temp = {
          roleid: props.params.roleid,
          roleName: roleListingData.role_name,
          roleDescription: roleListingData.role_desc,
          skillsRequired: roleListingData.skills.map(
            (skill) => skill.skill_name,
          ),
          roleDepartment: roleListingData.role_department,
          roleLocation: roleListingData.role_location,
          roleListingDesc: roleListingData.role_listing_desc,
        };
        setData(temp);
      })
      .catch((err) => {
        console.log("Error fetching role details:", err);
      });
  };
  useEffect(() => {
    fetchRoles();
  }, []);
  return (
    <>
      {data === undefined ? <div>Loading...</div> : <RoleListing data={data} />}
    </>
  );
};
export default RolePage;
